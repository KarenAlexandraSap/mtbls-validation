## METABOLIGHTS VALIDATION FRAMEWORK
MetaboLights validation framework is dynamic and based on [Open Policy Agent](https://www.openpolicyagent.org/) 



### Validation Rules and Default Metadata File Structure
| #  | SECTION | VALIDATION RULES | DEFAULT FILE COLUMNS |
|---|------------|--|--|
| 1  | ALL | [Validation Rules](docs/MetaboLightsRules.md) | - |
| 2  | INVESTIGATION FILE (i_Investigation.txt) | [Validation Rules](docs/validation-rules/investigation-validation-rules.md) | - |
| 3  | SAMPLE FILE (s_REQxxx.txt or s_MTBLSxxx.txt) | [Validation Rules](docs/validation-rules/sample-validation-rules.md) |[Default Sample File](docs/file-structures/sample-file-structure/sample-file.md) |
| 4  | ASSAY FILE (a_REQxxx.txt or a_MTBLSxxx.txt) | [Validation Rules](docs/validation-rules/assay-validation-rules.md) | [LC-MS](docs/file-structures/assay-file-structure/lc-ms.md), [GC-MS](docs/file-structures/assay-file-structure/gc-ms.md), [GCxGC-MS](docs/file-structures/assay-file-structure/gcxgc-ms.md), [DI-MS](docs/file-structures/assay-file-structure/di-ms.md), [FIA-MS](docs/file-structures/assay-file-structure/fia-ms.md), [LC-DAD](docs/file-structures/assay-file-structure/lc-dad.md), [CE-MS](docs/file-structures/assay-file-structure/ce-ms.md), [MS Imaging](docs/file-structures/assay-file-structure/msimaging.md), [GC-FID](docs/file-structures/assay-file-structure/gc-fid.md), [MALDI-MS](docs/file-structures/assay-file-structure/maldi-ms.md), [MS](docs/file-structures/assay-file-structure/ms.md), [NMR](docs/file-structures/assay-file-structure/nmr.md), [MR Imaging](docs/file-structures/assay-file-structure/mrimaging.md) |
| 5  | MAF FILE (m_REQxxx.tsv or a_MTBLSxxx.tsv) | [Validation Rules](docs/validation-rules/metabolite-validation-rules.md) | [MAF File for MS Assays](docs/file-structures/maf-file-structure/ms.md), [MAF File for NMR Assays](docs/file-structures/maf-file-structure/nmr.md) |
| 6  | DATA FILES | [Validation Rules](docs/validation-rules/file-validation-rules.md) | |



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
