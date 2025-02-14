| # |Header  | Column Structure  | Default Value  | Required | Min Length | Max Length | Controlled Terms |
|---|--------|-------------------|----------------|----------|------------|------------|------------------|
| 1 | Sample Name | single column |  | True | 1 | - | |
| 2 | Protocol REF | single column | Extraction | True | - | - | |
| 3 | Parameter Value[Extraction Method] | single column |  | False | - | - | |
| 4 | Extract Name | single column |  | False | - | - | |
| 5 | Protocol REF | single column | NMR sample | True | - | - | |
| 6 | Parameter Value[NMR tube type] | ontology column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/nmr.md#parameter-valuenmr-tube-type-column)|
| 7 | Parameter Value[Solvent] | ontology column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/nmr.md#parameter-valuesolvent-column)|
| 8 | Parameter Value[Sample pH] | single column |  | True | 1 | - | |
| 9 | Parameter Value[Temperature] | single column and unit ontology |  | True | 1 | - | |
| 10 | Labeled Extract Name | single column |  | False | - | - | |
| 11 | Label | ontology column |  | False | - | - | |
| 12 | Protocol REF | single column | NMR spectroscopy | True | - | - | |
| 13 | Parameter Value[Instrument] | ontology column |  | True | 1 | - | |
| 14 | Parameter Value[NMR Probe] | ontology column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/nmr.md#parameter-valuenmr-probe-column)|
| 15 | Parameter Value[Number of transients] | single column |  | True | 1 | - | |
| 16 | Parameter Value[Pulse sequence name] | single column |  | True | 1 | - | [Controlled Terms](../../../docs/prioritised-control-lists/assay-file-control-lists/nmr.md#parameter-valuepulse-sequence-name-column)|
| 17 | Parameter Value[Magnetic field strength] | single column and unit ontology |  | True | 1 | - | |
| 18 | Acquisition Parameter Data File | single column |  | False | - | - | |
| 19 | Protocol REF | single column | NMR assay | True | - | - | |
| 20 | NMR Assay Name | single column |  | False | - | - | |
| 21 | Free Induction Decay Data File | single column |  | False | - | - | |
| 22 | Protocol REF | single column | Data transformation | False | - | - | |
| 23 | Normalization Name | single column |  | False | - | - | |
| 24 | Derived Spectral Data File | single column |  | False | - | - | |
| 25 | Protocol REF | single column | Metabolite identification | True | - | - | |
| 26 | Data Transformation Name | single column |  | False | - | - | |
| 27 | Metabolite Assignment File | single column |  | True | 1 | - | |
