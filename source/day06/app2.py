# candidate to be app.py for python2.7 scrips

import sys
sys.path.append('modules')

import mastermedo

filename = 'input1'

filepath = 'data/' + filename + '.plain'

# @MasterMedo
mastermedo_run(filepath)
