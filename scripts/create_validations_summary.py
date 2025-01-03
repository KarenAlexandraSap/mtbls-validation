import datetime
import json

import pandas as pd

from scripts.models import PolicyMessageType, Violation
from scripts.utils import get_rules

metadata_lines = [
    "# METADATA",
    "# title:",
    "# description:",
    "# custom:",
    "#  rule_id:",
    "#  type:",
    "#  priority:",
    "#  section:",
]


def create_summary_files(rules: dict[str, pd.Series]):
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    version_file = "validation/metabolights/validation/v2/configuration/version.json"
    with open(version_file, "r") as f:
        version_content = json.loads(f.read())
    version = version_content["version"]

    violations_file = "json/violations.json"
    violations, summary = get_items(rules)
    violations_json = [x.model_dump() for x in violations]
    summary_json = [x.model_dump() for x in summary]
    versioned_content = {
        "validation_version": version,
        "created_at": now,
        "violations": violations_json,
        "summary": summary_json,
    }
    with open(violations_file, "w") as f:
        json.dump(versioned_content, f, indent=4)

    summary_file = "validation/metabolights/validation/v2/configuration/rules.json"
    with open(summary_file, "w") as f:
        json.dump({"rules": versioned_content}, f, indent=4)
    with open("docs/MetaboLightsRules.md", "w") as f:
        f.write(
            "| # |RULE ID              | TYPE                | TITLE                    | DESCRIPTION                  |\n"
        )
        f.write(
            "|---|---------------------|---------------------|--------------------------|------------------------------|\n"
        )
        for idx, item in enumerate(violations):
            f.write(
                f"| {idx + 1} | {item.rule_id} | {item.type.value} | {item.title} | {item.description} |\n"
            )


def get_items(rules):
    violations: list[Violation] = []
    summary: list[Violation] = []
    for rule_id, rule in rules.items():
        item = Violation(
            rule_id=rule_id,
            title=str(rule["TITLE"]).strip(),
            description=str(rule["DESCRIPTION"]).strip(),
            type=PolicyMessageType(
                str(rule["TYPE"].strip()) if rule["TYPE"] else PolicyMessageType.INFO
            ),
        )
        if len(rule_id) < 15:
            summary.append(item)
        else:
            violations.append(item)
    for items in (violations, summary):
        items.sort(key=lambda x: x.type.value + x.rule_id)
    return violations, summary


if __name__ == "__main__":
    rules = get_rules()
    create_summary_files(rules)
