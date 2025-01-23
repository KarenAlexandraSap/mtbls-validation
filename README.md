## METABOLIGHTS VALIDATION FRAMEWORK
MetaboLights validation framework is dynamic and based on [Open Policy Agent](https://www.openpolicyagent.org/) 



### Validation Rules and Default Metadata File Structure
| #  | SECTION | VALIDATION RULES | DEFAULT FILE COLUMNS | PRIORITISED CONTROL LISTS|
|---|------------|--|--|--|
| 1  | ALL | [Validation Rules](docs/MetaboLightsRules.md) | - | - |
| 2  | INVESTIGATION FILE (i_Investigation.txt) | [Validation Rules](docs/validation-rules/investigation-validation-rules.md) | [Prioritised Control Lists](docs/prioritised-control-lists/investigation-file-control-lists/investigation-file.md) |
| 3  | SAMPLE FILE (s_REQxxx.txt or s_MTBLSxxx.txt) | [Validation Rules](docs/validation-rules/sample-validation-rules.md) |[Default Sample File](docs/file-structures/sample-file-structure/sample-file.md) | [Characteristics & Factors](docs/prioritised-control-lists/sample-file-control-lists/sample-file.md), [Units](docs/prioritised-control-lists/unit-columns-control-lists/unit-columns.md) |
| 4  | ASSAY FILE (a_REQxxx.txt or a_MTBLSxxx.txt) | [Validation Rules](docs/validation-rules/assay-validation-rules.md) | [LC-MS](docs/file-structures/assay-file-structure/lc-ms.md), [GC-MS](docs/file-structures/assay-file-structure/gc-ms.md), [GCxGC-MS](docs/file-structures/assay-file-structure/gcxgc-ms.md), [DI-MS](docs/file-structures/assay-file-structure/di-ms.md), [FIA-MS](docs/file-structures/assay-file-structure/fia-ms.md), [LC-DAD](docs/file-structures/assay-file-structure/lc-dad.md), [CE-MS](docs/file-structures/assay-file-structure/ce-ms.md), [MS Imaging](docs/file-structures/assay-file-structure/msimaging.md), [GC-FID](docs/file-structures/assay-file-structure/gc-fid.md), [MALDI-MS](docs/file-structures/assay-file-structure/maldi-ms.md), [MS](docs/file-structures/assay-file-structure/ms.md), [NMR](docs/file-structures/assay-file-structure/nmr.md), [MR Imaging](docs/file-structures/assay-file-structure/mrimaging.md) | [LC-MS](docs/prioritised-control-lists/assay-file-control-lists/lc-ms.md), [GC-MS](docs/prioritised-control-lists/assay-file-control-lists/gc-ms.md), [FIA-MS](docs/prioritised-control-lists/assay-file-control-lists/fia-ms.md), [DI-MS](docs/prioritised-control-lists/assay-file-control-lists/di-ms.md), [GCxGC-MS](docs/prioritised-control-lists/assay-file-control-lists/gcxgc-ms.md), [MALDI-MS](docs/prioritised-control-lists/assay-file-control-lists/maldi-ms.md), [MSImaging](docs/prioritised-control-lists/assay-file-control-lists/msimaging.md), [NMR](docs/prioritised-control-lists/assay-file-control-lists/nmr.md), [Units](docs/prioritised-control-lists/unit-columns-control-lists/unit-columns.md) |
| 5  | MAF FILE (m_REQxxx.tsv or a_MTBLSxxx.tsv) | [Validation Rules](docs/validation-rules/metabolite-validation-rules.md) | [MAF File for MS Assays](docs/file-structures/maf-file-structure/ms.md), [MAF File for NMR Assays](docs/file-structures/maf-file-structure/nmr.md) |  | 
| 6  | DATA FILES | [Validation Rules](docs/validation-rules/file-validation-rules.md) | | |



## Open Policy Agent Deployment 

### Development with vscode
- Install Open Policy Agent extension (tsandall.opa)
- Download opa executable from [here](https://www.openpolicyagent.org/docs/latest/#running-opa)


### Run and test validation
```
cd validation
opa test . -v
opa build  --ignore tests .
```
