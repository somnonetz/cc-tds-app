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
%1. Variante
  tds:
		type: array[]
		inputBinding:
		prefix: tds
		itemSeparator: ","
		separate: false
		
%2. Variante, overall array separated		
  tds:
		type: array
		items:array type:int[]
		inputBinding:
		prefix: tds
		itemSeparator: ","
		separate: false	
		
