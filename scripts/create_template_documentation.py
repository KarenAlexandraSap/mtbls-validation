import json
from pathlib import Path

if __name__ == "__main__":
    templates_path = "validation/metabolights/validation/v2/templates"
    sample_file_templates = [f"{templates_path}/sampleFileHeaderTemplates.json"]
    assay_file_templates = [
        str(x)
        for x in Path(f"{templates_path}/assayFileHeaderTemplates").glob("*.json")
    ]
    assignment_file_templates = [
        str(x)
        for x in Path(f"{templates_path}/assignmentFileHeaderTemplates").glob("*.json")
    ]

    pairs = [
        (sample_file_templates, "sample-file-structure"),
        (assay_file_templates, "assay-file-structure"),
        (assignment_file_templates, "maf-file-structure"),
    ]
    for file_paths, folder in pairs:
        for file in file_paths:
            file_path = Path(file)
            with file_path.open() as f:
                file_content = json.load(f)

            for name, templates in file_content.items():
                doc_file_name = (
                    f"{folder.removesuffix('-structure')}.md"
                    if len(file_paths) == 1
                    else f"{name.lower()}.md"
                )
                headers = templates[0]["headers"]

                target_path = Path(f"docs/file-structures/{folder}/{doc_file_name}")

                target_path.parent.mkdir(parents=True, exist_ok=True)
                with target_path.open("w") as f:
                    f.write(
                        "| # |Header  | Column Structure  | Default Value  | Required | Min Length | Max Length |\n"
                        "|---|--------|-------------------|----------------|----------|------------|------------|\n"
                    )
                    for idx, item in enumerate(headers):
                        f.write(
                            f"| {idx + 1} "
                            f"| {item['columnHeader']} "
                            f"| {item['columnStructure'].lower().replace('_', ' ')} "
                            f"| {item['defaultValue'] if item['defaultValue'] else ''} "
                            f"| {item['required']} "
                            f"| {item['minLength'] if item['minLength'] > 0 else '-'} "
                            f"| {item['maxLength'] if item['maxLength'] > 0 else '-'} "
                            "|\n"
                        )
