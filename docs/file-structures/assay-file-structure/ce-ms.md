| # |Header  | Column Structure  | Default Value  | Required | Min Length | Max Length | Controlled Terms |
|---|--------|-------------------|----------------|----------|------------|------------|------------------|
| 1 | Sample Name | single column |  | True | 1 | - | |
| 2 | Protocol REF | single column | Extraction | True | - | - | |
| 3 | Parameter Value[Post Extraction] | single column |  | False | - | - | |
| 4 | Parameter Value[Derivatization] | single column |  | False | - | - | |
| 5 | Extract Name | single column |  | False | - | - | |
| 6 | Protocol REF | single column | Capillary Electrophoresis | True | - | - | |
| 7 | Parameter Value[CE Instrument] | single column |  | True | 5 | - | |
| 8 | Parameter Value[Column model] | single column |  | True | 1 | - | |
| 9 | Parameter Value[Column type] | single column |  | True | 1 | - | |
| 10 | Labeled Extract Name | single column |  | False | - | - | |
| 11 | Label | ontology column |  | False | - | - | |
| 12 | Protocol REF | single column | Mass spectrometry | True | - | - | |
| 13 | Parameter Value[Scan polarity] | single column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/ce-ms.md#parameter-valuescan-polarity-column)|
| 14 | Parameter Value[Scan m/z range] | single column |  | True | 1 | - | |
| 15 | Parameter Value[Instrument] | ontology column |  | True | 1 | - | |
| 16 | Parameter Value[Ion source] | ontology column |  | False | - | - | |
| 17 | Parameter Value[Mass analyzer] | ontology column |  | False | - | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/ce-ms.md#parameter-valuemass-analyzer-column)|
| 18 | MS Assay Name | single column |  | False | - | - | |
| 19 | Raw Spectral Data File | single column |  | False | - | - | |
| 20 | Protocol REF | single column | Data transformation | True | - | - | |
| 21 | Normalization Name | single column |  | False | - | - | |
| 22 | Derived Spectral Data File | single column |  | False | - | - | |
| 23 | Protocol REF | single column | Metabolite identification | True | - | - | |
| 24 | Data Transformation Name | single column |  | False | - | - | |
| 25 | Metabolite Assignment File | single column |  | True | 1 | - | |
