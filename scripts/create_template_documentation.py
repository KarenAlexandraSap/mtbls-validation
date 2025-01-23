import json
from pathlib import Path
from typing import Any, OrderedDict, Tuple

from pydantic import BaseModel


class OntologyTerm(BaseModel):
    source_ref: str = ""
    term_accession: str = ""
    term: str = ""


def create_recommended_assay_control_lists():
    templates_path = "validation/metabolights/validation/v2/controlLists/assayColumns"
    assay_file_templates = [str(x) for x in Path(f"{templates_path}").glob("*.json")]

    recommended_terms_path = "docs/prioritised-control-lists"
    recommended_terms: OrderedDict[str, OrderedDict[str, list[OntologyTerm]]] = (
        OrderedDict()
    )

    for file in assay_file_templates:
        file_path = Path(file)
        with file_path.open() as f:
            file_content = json.load(f)

        for name, template in file_content.items():
            control_list = template["controlList"]
            techniques = control_list[0]["techniques"]
            values = control_list[0]["values"]
            terms = [
                OntologyTerm(
                    term=x["term"],
                    source_ref=x["termSourceRef"],
                    term_accession=x["termAccessionNumber"],
                )
                for x in values
            ]
            terms.sort(key=lambda x: x.term + x.source_ref)
            column_name = name
            for technique in techniques:
                if technique not in recommended_terms:
                    recommended_terms[technique] = OrderedDict()

                recommended_terms[technique][column_name] = terms

    target_parent_path = Path(f"{recommended_terms_path}/assay-file-control-lists")

    target_parent_path.mkdir(parents=True, exist_ok=True)
    for technique, column_terms in recommended_terms.items():
        target_path = target_parent_path / Path(f"{technique.lower()}.md")

        with target_path.open("w") as f:
            f.write(f"# {technique} Assay File Prioritised Control Lists Terms\n")
            sorted_column_terms = [(key, value) for key, value in column_terms.items()]
            sorted_column_terms.sort(key=lambda x: x[0])
            for column_name, terms in sorted_column_terms:
                f.write(f"\n### {column_name} Column\n\n")
                f.write(
                    "| # |Term  | Term Source  | Term Accession |\n"
                    "|---|------|--------------|----------------|\n"
                )
                for idx, item in enumerate(terms):
                    f.write(
                        f"| {idx + 1} "
                        f"| {item.term} "
                        f"| {item.source_ref} "
                        f"| {item.term_accession} "
                        "|\n"
                    )


def create_recommended_control_lists(
    templates_path: str, title: str = None, file_name: str = None
):
    field_control_list_path = [str(x) for x in Path(f"{templates_path}").glob("*.json")]

    recommended_terms_path = "docs/prioritised-control-lists"
    target_parent_path = Path(f"{recommended_terms_path}/{file_name}-control-lists")
    target_parent_path.mkdir(parents=True, exist_ok=True)
    recommended_terms: OrderedDict[str, list[OntologyTerm]] = OrderedDict()
    target_path = target_parent_path / Path(f"{file_name}.md")
    column_attributes: OrderedDict[str, Tuple[Any, bool, bool]] = OrderedDict()
    with target_path.open("w") as fw:
        for file in field_control_list_path:
            file_path = Path(file)
            with file_path.open() as f:
                file_content = json.load(f)
            name = list(file_content.keys())[0]
            control_list = file_content[name]["terms"]
            terms = [
                OntologyTerm(
                    term=x["term"],
                    source_ref=x["termSourceRef"],
                    term_accession=x["termAccessionNumber"],
                )
                for x in control_list
            ]
            terms.sort(key=lambda x: x.term + x.source_ref)
            recommended_terms[name] = terms
            column_attributes[name] = (
                file_content[name]["ontologies"],
                file_content[name]["additionalOntologies"],
                file_content[name]["additionalTerms"],
            )

        fw.write(f"# {title} Prioritised Control Lists Terms\n")
        sorted_fields = [(key, value) for key, value in recommended_terms.items()]
        sorted_fields.sort(key=lambda x: x[0])

        for name, terms in sorted_fields:
            fw.write(f"\n### {name} \n\n")
            fw.write("\n#### Configuration \n\n")
            fw.write(
                "| Parameter | Value  |\n"
                "|--------|--------|\n"
                f"| Prioritised Ontologies | {', '.join(column_attributes[name][0])}|\n"
                f"| Additional Ontologies Allowed | {column_attributes[name][1]}|\n"
                f"| Additional Terms Allowed | {column_attributes[name][2]}|\n"
                "\n"
            )

            fw.write("\n#### Terms \n\n")
            fw.write(
                "| # |Term  | Term Source  | Term Accession |\n"
                "|---|------|--------------|----------------|\n"
            )
            for idx, item in enumerate(terms):
                fw.write(
                    f"| {idx + 1} "
                    f"| {item.term} "
                    f"| {item.source_ref} "
                    f"| {item.term_accession} "
                    "|\n"
                )


def create_file_stucture_documentation():
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


if __name__ == "__main__":
    create_file_stucture_documentation()
    create_recommended_assay_control_lists()
    templates_path = (
        "validation/metabolights/validation/v2/controlLists/investigationFile"
    )
    file_name = "investigation-file"
    title = "Investigation File"
    create_recommended_control_lists(
        templates_path=templates_path, file_name=file_name, title=title
    )
    templates_path = "validation/metabolights/validation/v2/controlLists/sampleColumns"
    file_name = "sample-file"
    title = "Sample File"
    create_recommended_control_lists(
        templates_path=templates_path, file_name=file_name, title=title
    )

    templates_path = "validation/metabolights/validation/v2/controlLists/unitColumns"
    file_name = "unit-columns"
    title = "Unit Columns"
    create_recommended_control_lists(
        templates_path=templates_path, file_name=file_name, title=title
    )
