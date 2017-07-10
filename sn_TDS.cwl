cwlVersion: v1.0
class: CommandLineTool
baseCommand: run_sn_TDS.sh

inputs:
  MCRroot:
    type: string
    inputBinding:
      separate: false
      position: 1
  data:
    type: string
    inputBinding:
      prefix: data 
      separate: false
  montage_filename:
    type: string?
    inputBinding:
	  prefix: montage_filename
  resultpath:
    type: string?
    inputBinding:
      prefix: resultpath
  outputfilebase:
    type: string?
    inputBinding:
      prefix: outputfilebase			
  wl_sfe:
    type: int?
    inputBinding:
      prefix: wl_sfe
  ws_sfe:
    type: int?
    inputBinding:
      prefix: ws_sfe
  wl_xcc:
    type: int?
    inputBinding:
      prefix: wl_xcc
  ws_xcc:
    type: int?
    inputBinding:
      prefix: ws_xcc
  wl_tds:
    type: int?
    inputBinding:
      prefix: wl_tds
  ws_tds:
    type: int?
    inputBinding:
      prefix: ws_tds
  mld_tds:
    type: float?
    inputBinding:
      prefix: mld_tds		

outputs:
  tds_all:
    type: File
    outputBinding:
      glob: "*_getTDS_all.mat"
  tds_result:
    type: File
    outputBinding:
      glob: "*_getTDS.mat"

