| # |Header  | Column Structure  | Default Value  | Required | Min Length | Max Length | Controlled Terms |
|---|--------|-------------------|----------------|----------|------------|------------|------------------|
| 1 | Sample Name | single column |  | True | 1 | - | |
| 2 | Protocol REF | single column | Extraction | True | - | - | |
| 3 | Parameter Value[Post Extraction] | single column |  | False | - | - | |
| 4 | Parameter Value[Derivatization] | single column |  | False | - | - | |
| 5 | Extract Name | single column |  | False | - | - | |
| 6 | Labeled Extract Name | single column |  | False | - | - | |
| 7 | Label | ontology column |  | False | - | - | |
| 8 | Protocol REF | single column | Mass spectrometry | True | - | - | |
| 9 | Parameter Value[Scan polarity] | single column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/maldi-ms.md#parameter-valuescan-polarity-column)|
| 10 | Parameter Value[Scan m/z range] | single column |  | True | 1 | - | |
| 11 | Parameter Value[Instrument] | ontology column |  | True | 1 | - | |
| 12 | Parameter Value[Ion source] | single column |  | False | - | - | |
| 13 | Parameter Value[Mass analyzer] | single column |  | False | - | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/maldi-ms.md#parameter-valuemass-analyzer-column)|
| 14 | MS Assay Name | single column |  | False | - | - | |
| 15 | Raw Spectral Data File | single column |  | False | - | - | |
| 16 | Protocol REF | single column | Data transformation | True | - | - | |
| 17 | Normalization Name | single column |  | False | - | - | |
| 18 | Derived Spectral Data File | single column |  | False | - | - | |
| 19 | Protocol REF | single column | Metabolite identification | True | - | - | |
| 20 | Data Transformation Name | single column |  | False | - | - | |
| 21 | Metabolite Assignment File | single column |  | True | 1 | - | |
