import sys
import json
from subprocess import call

MATLAB_HOME = '/usr/local/MATLAB/MATLAB_Runtime/v85'
DATA_FILE_PATH = '/root/input_files/polysomnography.edf'
MONTAGE_FILE_PATH = '/root/montage.txt'

command = ['bash', '/root/run_sn_TDS.sh', MATLAB_HOME, 'data', DATA_FILE_PATH]

montage = None
try:
    parameters = json.loads(sys.argv[1])
    montage = parameters['montage']
except:
    pass

if montage:
    with open(MONTAGE_FILE_PATH, 'w') as f:
        for channel_type in montage:
            print(channel_type, file=f)

    command += ['montage_filepath', MONTAGE_FILE_PATH]

return_code = call(command)

sys.exit(return_code)
