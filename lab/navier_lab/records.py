"""Validate the research control-plane records without third-party packages."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
RECORDS_DIR = Path("dossier/records")

SOURCE_FIELDS = {
    "id",
    "title",
    "authors",
    "year",
    "kind",
    "url",
    "version",
    "primary",
    "status",
    "last_checked",
    "notes",
}
CLAIM_FIELDS = {
    "id",
    "plain",
    "formal",
    "domain",
    "forcing",
    "solution_class",
    "assumptions",
    "conclusion",
    "scaling",
    "status",
    "source_ids",
    "depends_on",
    "audit",
    "last_checked",
}
ROUTE_FIELDS = {
    "id",
    "parent",
    "side",
    "title",
    "question",
    "entry_assumptions",
    "success",
    "kill_criterion",
    "status",
    "children",
    "evidence_claim_ids",
}
EXPERIMENT_FIELDS = {
    "id",
    "title",
    "kind",
    "route_ids",
    "claim_ids",
    "hypothesis",
    "invariants",
    "method",
    "certificate",
    "success_criterion",
    "failure_interpretation",
    "status",
    "artifacts",
    "last_run",
}
OBLIGATION_FIELDS = {
    "id",
    "stage",
    "statement",
    "status",
    "depends_on",
    "evidence",
    "disposition",
}

SOURCE_STATUSES = {"official", "peer_reviewed", "preprint", "translation"}
CLAIM_STATUSES = {
    "official_status",
    "definition",
    "established",
    "conditional_preprint",
    "preprint_claim",
    "open",
}
ROUTE_STATUSES = {"program", "open", "partial", "closed"}
EXPERIMENT_STATUSES = {"planned", "implemented", "running", "complete", "failed"}
OBLIGATION_STATUSES = {
    "open",
    "partially_mechanized",
    "verified",
    "repaired",
    "unsupported",
}


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.errors: list[str] = []

    def error(self, location: str, message: str) -> None:
        self.errors.append(f"{location}: {message}")

    def load(self, relative_path: str) -> dict[str, Any]:
        path = self.root / relative_path
        try:
            with path.open(encoding="utf-8") as handle:
                value = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            self.error(relative_path, str(exc))
            return {}
        if not isinstance(value, dict):
            self.error(relative_path, "top-level JSON value must be an object")
            return {}
        if value.get("schema_version") != 1:
            self.error(relative_path, "schema_version must equal 1")
        return value

    def require_fields(
        self, location: str, record: dict[str, Any], fields: set[str]
    ) -> None:
        missing = sorted(fields - record.keys())
        if missing:
            self.error(location, f"missing fields: {', '.join(missing)}")
        unknown = sorted(record.keys() - fields)
        if unknown:
            self.error(location, f"unknown fields: {', '.join(unknown)}")

    def require_nonempty_string(
        self, location: str, record: dict[str, Any], field: str
    ) -> None:
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            self.error(location, f"{field} must be a nonempty string")

    def require_string_list(
        self, location: str, record: dict[str, Any], field: str
    ) -> None:
        value = record.get(field)
        if not isinstance(value, list) or any(
            not isinstance(item, str) or not item for item in value
        ):
            self.error(location, f"{field} must be a list of nonempty strings")

    def require_date(self, location: str, value: Any, field: str) -> None:
        if not isinstance(value, str):
            self.error(location, f"{field} must be an ISO date")
            return
        try:
            date.fromisoformat(value)
        except ValueError:
            self.error(location, f"{field} is not an ISO date: {value}")

    def unique_map(
        self, kind: str, records: Iterable[dict[str, Any]]
    ) -> dict[str, dict[str, Any]]:
        result: dict[str, dict[str, Any]] = {}
        for index, record in enumerate(records):
            identifier = record.get("id")
            location = f"{kind}[{index}]"
            if not isinstance(identifier, str) or not identifier:
                self.error(location, "id must be a nonempty string")
                continue
            if identifier in result:
                self.error(location, f"duplicate id {identifier}")
            result[identifier] = record
        return result

    def validate(self) -> dict[str, int]:
        source_data = self.load(f"{RECORDS_DIR}/sources.json")
        claim_data = self.load(f"{RECORDS_DIR}/claims.json")
        route_data = self.load(f"{RECORDS_DIR}/routes.json")
        experiment_data = self.load(f"{RECORDS_DIR}/experiments.json")
        obligation_data = self.load(
            f"{RECORDS_DIR}/paper-2607-obligations.json"
        )

        sources = self._list(source_data, "sources", "sources.json")
        claims = self._list(claim_data, "claims", "claims.json")
        routes = self._list(route_data, "routes", "routes.json")
        experiments = self._list(
            experiment_data, "experiments", "experiments.json"
        )
        obligations = self._list(
            obligation_data, "obligations", "paper-2607-obligations.json"
        )

        source_map = self.unique_map("sources", sources)
        claim_map = self.unique_map("claims", claims)
        route_map = self.unique_map("routes", routes)
        experiment_map = self.unique_map("experiments", experiments)
        obligation_map = self.unique_map("obligations", obligations)

        self._validate_sources(sources)
        self._validate_claims(claims, source_map, claim_map)
        self._validate_routes(routes, route_map, claim_map)
        self._validate_experiments(experiments, route_map, claim_map)
        self._validate_obligations(
            obligations, obligation_map, experiment_map, source_map, obligation_data
        )

        return {
            "sources": len(source_map),
            "claims": len(claim_map),
            "routes": len(route_map),
            "experiments": len(experiment_map),
            "obligations": len(obligation_map),
        }

    def _list(
        self, data: dict[str, Any], field: str, filename: str
    ) -> list[dict[str, Any]]:
        value = data.get(field, [])
        if not isinstance(value, list):
            self.error(filename, f"{field} must be a list")
            return []
        if any(not isinstance(item, dict) for item in value):
            self.error(filename, f"every {field} item must be an object")
            return [item for item in value if isinstance(item, dict)]
        return value

    def _validate_sources(self, sources: list[dict[str, Any]]) -> None:
        for index, record in enumerate(sources):
            location = f"sources[{index}]"
            self.require_fields(location, record, SOURCE_FIELDS)
            for field in ("id", "title", "kind", "url", "version", "status", "notes"):
                self.require_nonempty_string(location, record, field)
            self.require_string_list(location, record, "authors")
            if not isinstance(record.get("year"), int):
                self.error(location, "year must be an integer")
            if not isinstance(record.get("primary"), bool):
                self.error(location, "primary must be boolean")
            if record.get("status") not in SOURCE_STATUSES:
                self.error(location, f"invalid status {record.get('status')}")
            url = record.get("url")
            if isinstance(url, str) and not url.startswith(("https://", "http://")):
                self.error(location, "url must be HTTP(S)")
            self.require_date(location, record.get("last_checked"), "last_checked")

    def _validate_claims(
        self,
        claims: list[dict[str, Any]],
        sources: dict[str, dict[str, Any]],
        claim_map: dict[str, dict[str, Any]],
    ) -> None:
        for index, record in enumerate(claims):
            location = f"claims[{index}]"
            self.require_fields(location, record, CLAIM_FIELDS)
            for field in (
                "id",
                "plain",
                "formal",
                "domain",
                "forcing",
                "solution_class",
                "conclusion",
                "scaling",
                "status",
                "audit",
            ):
                self.require_nonempty_string(location, record, field)
            for field in ("assumptions", "source_ids", "depends_on"):
                self.require_string_list(location, record, field)
            if record.get("status") not in CLAIM_STATUSES:
                self.error(location, f"invalid status {record.get('status')}")
            self.require_date(location, record.get("last_checked"), "last_checked")
            self._check_refs(location, record.get("source_ids"), sources, "source")
            self._check_refs(location, record.get("depends_on"), claim_map, "claim")
            if record.get("id") in record.get("depends_on", []):
                self.error(location, "claim cannot depend on itself")

    def _validate_routes(
        self,
        routes: list[dict[str, Any]],
        route_map: dict[str, dict[str, Any]],
        claim_map: dict[str, dict[str, Any]],
    ) -> None:
        roots: list[str] = []
        for index, record in enumerate(routes):
            location = f"routes[{index}]"
            self.require_fields(location, record, ROUTE_FIELDS)
            for field in (
                "id",
                "side",
                "title",
                "question",
                "success",
                "kill_criterion",
                "status",
            ):
                self.require_nonempty_string(location, record, field)
            for field in ("entry_assumptions", "children", "evidence_claim_ids"):
                self.require_string_list(location, record, field)
            if record.get("status") not in ROUTE_STATUSES:
                self.error(location, f"invalid status {record.get('status')}")
            parent = record.get("parent")
            if parent is None:
                if isinstance(record.get("id"), str):
                    roots.append(record["id"])
            elif not isinstance(parent, str) or parent not in route_map:
                self.error(location, f"unknown parent {parent}")
            self._check_refs(location, record.get("children"), route_map, "route")
            self._check_refs(
                location, record.get("evidence_claim_ids"), claim_map, "claim"
            )

        if roots != ["ROUTE-ROOT"]:
            self.error("routes", f"expected sole root ROUTE-ROOT, found {roots}")

        for identifier, record in route_map.items():
            parent = record.get("parent")
            if isinstance(parent, str) and identifier not in route_map[parent].get(
                "children", []
            ):
                self.error(identifier, f"parent {parent} does not list this child")
            for child in record.get("children", []):
                if child in route_map and route_map[child].get("parent") != identifier:
                    self.error(identifier, f"child {child} points to another parent")

        visited: set[str] = set()
        active: set[str] = set()

        def walk(identifier: str) -> None:
            if identifier in active:
                self.error("routes", f"cycle detected at {identifier}")
                return
            if identifier in visited or identifier not in route_map:
                return
            active.add(identifier)
            for child in route_map[identifier].get("children", []):
                walk(child)
            active.remove(identifier)
            visited.add(identifier)

        walk("ROUTE-ROOT")
        unreachable = sorted(route_map.keys() - visited)
        if unreachable:
            self.error("routes", f"unreachable routes: {', '.join(unreachable)}")

    def _validate_experiments(
        self,
        experiments: list[dict[str, Any]],
        route_map: dict[str, dict[str, Any]],
        claim_map: dict[str, dict[str, Any]],
    ) -> None:
        for index, record in enumerate(experiments):
            location = f"experiments[{index}]"
            self.require_fields(location, record, EXPERIMENT_FIELDS)
            for field in (
                "id",
                "title",
                "kind",
                "hypothesis",
                "method",
                "certificate",
                "success_criterion",
                "failure_interpretation",
                "status",
            ):
                self.require_nonempty_string(location, record, field)
            for field in ("route_ids", "claim_ids", "invariants", "artifacts"):
                self.require_string_list(location, record, field)
            if record.get("status") not in EXPERIMENT_STATUSES:
                self.error(location, f"invalid status {record.get('status')}")
            self._check_refs(location, record.get("route_ids"), route_map, "route")
            self._check_refs(location, record.get("claim_ids"), claim_map, "claim")
            if record.get("status") in {"implemented", "running", "complete"}:
                for artifact in record.get("artifacts", []):
                    if not (self.root / artifact).exists():
                        self.error(location, f"missing implemented artifact {artifact}")
            last_run = record.get("last_run")
            if last_run is not None:
                self.require_date(location, last_run, "last_run")

    def _validate_obligations(
        self,
        obligations: list[dict[str, Any]],
        obligation_map: dict[str, dict[str, Any]],
        experiment_map: dict[str, dict[str, Any]],
        source_map: dict[str, dict[str, Any]],
        obligation_data: dict[str, Any],
    ) -> None:
        paper_id = obligation_data.get("paper_id")
        if paper_id not in source_map:
            self.error("paper-2607-obligations.json", f"unknown paper_id {paper_id}")
        for index, record in enumerate(obligations):
            location = f"obligations[{index}]"
            self.require_fields(location, record, OBLIGATION_FIELDS)
            for field in ("id", "stage", "statement", "status", "disposition"):
                self.require_nonempty_string(location, record, field)
            for field in ("depends_on", "evidence"):
                self.require_string_list(location, record, field)
            if record.get("status") not in OBLIGATION_STATUSES:
                self.error(location, f"invalid status {record.get('status')}")
            self._check_refs(
                location, record.get("depends_on"), obligation_map, "obligation"
            )
            self._check_refs(
                location, record.get("evidence"), experiment_map, "experiment"
            )
            if record.get("id") in record.get("depends_on", []):
                self.error(location, "obligation cannot depend on itself")

    def _check_refs(
        self,
        location: str,
        values: Any,
        target: dict[str, dict[str, Any]],
        kind: str,
    ) -> None:
        if not isinstance(values, list):
            return
        missing = [value for value in values if value not in target]
        if missing:
            self.error(location, f"unknown {kind} refs: {', '.join(missing)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=REPOSITORY_ROOT,
        help="repository root",
    )
    arguments = parser.parse_args(argv)
    validator = Validator(arguments.root.resolve())
    counts = validator.validate()
    if validator.errors:
        print("record validation failed:", file=sys.stderr)
        for error in validator.errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    summary = ", ".join(f"{kind}={count}" for kind, count in counts.items())
    print(f"record validation OK: {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
