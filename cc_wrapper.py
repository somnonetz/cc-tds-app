import sys
import json
from subprocess import call

command = [
    'bash', '/app/run_sn_TDS.sh', '/usr/local/MATLAB/MATLAB_Runtime/v85',
    'data', '/root/input_files/psg.edf',
    'montage_filename', '/root/input_files/montage.txt',
    'resultpath', '/root/result_files'
]

possible_parameters = [
    'wl_sfe',
    'ws_sfe',
    'wl_xcc',
    'ws_xcc',
    'wl_tds',
    'ws_tds',
    'mld_tds',
    'mlf_tds',
    'debug'
]

parameters = None
try:
    parameters = json.loads(sys.argv[1])
except:
    pass

if parameters:
    for pp in possible_parameters:
        if parameters.get(pp):
            command += [pp, parameters[pp]]

return_code = call(command)

sys.exit(return_code)
