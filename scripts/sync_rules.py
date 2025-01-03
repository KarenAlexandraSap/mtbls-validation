import glob

import pandas as pd

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


def update_files(rules: dict[str, pd.Series]):
    files = [
        x
        for x in glob.iglob("./validation/**/*.rego", recursive=True)
        if not x.endswith("_test.rego")
    ]
    for file in files:
        rows = []
        updated: bool = False
        with open(file, "r") as f:
            rows = f.readlines()
            total_lines = len(rows)
            for line in range(total_lines):
                if (line + 5) < total_lines:
                    metadata_header = True
                    for i in range(8):
                        if not rows[line + i].startswith(metadata_lines[i]):
                            metadata_header = False
                            break
                    if metadata_header:
                        rule_id = rows[line + 4].split(":")[1].strip()
                        if rule_id in rules:
                            rule = rules[rule_id]
                            updated = True
                            rows[line + 1] = get_value(rule, "title")
                            rows[line + 2] = get_value(rule, "description")
                            rows[line + 5] = get_value(rule, "type", "  ")
                            rows[line + 6] = get_value(rule, "priority", "  ")
                            rows[line + 7] = get_value(rule, "section", "  ")

        if updated:
            print(f"Updating file: {file}")
            with open(file, "w") as f:
                f.writelines(rows)


def get_value(rule, key: str, padding: str = " "):
    return (
        f"#{padding}{key}: "
        + " ".join(rule[key.upper()].strip().split()).replace(":", " ")
        + "\n"
    )


if __name__ == "__main__":
    rules = get_rules()
    update_files(rules)
