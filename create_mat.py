import sys
import os
import glob
import numpy as np
from scipy.io import savemat

input_dir = sys.argv[1]
if not os.path.isdir(input_dir):
    raise ValueError('Please enter a valid directory')
if not input_dir.endswith('/'):
    input_dir += '/'

data = {}
file_list = glob.glob(os.path.join(input_dir,"*.npy"))
if not file_list:
    raise RuntimeError('No .npy file found in {}'.format(input_dir))

file_list.sort()
for f in file_list:
    item_name = os.path.splitext(os.path.basename(f))[0]
    data[item_name] = np.load(f)

outfile = os.path.join(input_dir, os.path.dirname(input_dir)+'.mat')
print('output file', outfile)
savemat(outfile, data)
