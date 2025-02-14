| # |Header  | Column Structure  | Default Value  | Required | Min Length | Max Length | Controlled Terms |
|---|--------|-------------------|----------------|----------|------------|------------|------------------|
| 1 | Sample Name | single column |  | True | 1 | - | |
| 2 | Protocol REF | single column | Extraction | True | - | - | |
| 3 | Parameter Value[Post Extraction] | single column |  | False | - | - | |
| 4 | Parameter Value[Derivatization] | single column |  | False | - | - | |
| 5 | Extract Name | single column |  | False | - | - | |
| 6 | Protocol REF | single column | Chromatography | True | - | - | |
| 7 | Parameter Value[Chromatography Instrument] | ontology column |  | True | 5 | - | |
| 8 | Parameter Value[Autosampler model] | single column |  | False | - | - | |
| 9 | Parameter Value[Column model] | single column |  | True | 5 | - | |
| 10 | Parameter Value[Column type] | single column |  | True | 5 | - | |
| 11 | Parameter Value[Guard column] | single column |  | False | - | - | |
| 12 | Labeled Extract Name | single column |  | False | - | - | |
| 13 | Label | ontology column |  | False | - | - | |
| 14 | Protocol REF | single column | Mass spectrometry | True | - | - | |
| 15 | Parameter Value[Scan polarity] | single column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/gc-ms.md#parameter-valuescan-polarity-column)|
| 16 | Parameter Value[Scan m/z range] | single column |  | True | 1 | - | |
| 17 | Parameter Value[Instrument] | ontology column |  | True | 1 | - | |
| 18 | Parameter Value[Ion source] | ontology column |  | False | - | - | |
| 19 | Parameter Value[Mass analyzer] | ontology column |  | False | - | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/gc-ms.md#parameter-valuemass-analyzer-column)|
| 20 | MS Assay Name | single column |  | False | - | - | |
| 21 | Raw Spectral Data File | single column |  | False | - | - | |
| 22 | Protocol REF | single column | Data transformation | False | - | - | |
| 23 | Normalization Name | single column |  | False | - | - | |
| 24 | Derived Spectral Data File | single column |  | False | - | - | |
| 25 | Protocol REF | single column | Metabolite identification | True | - | - | |
| 26 | Data Transformation Name | single column |  | False | - | - | |
| 27 | Metabolite Assignment File | single column |  | True | 1 | - | |
