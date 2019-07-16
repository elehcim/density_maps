# select a snapshot, cut on the density and provide a mat file with particle positions (x,y,z)

import pynbody
import numpy as np
import sys
import os
import glob
import numpy as np
from scipy.io import savemat




def convert_snapshot_to_mat(snap_name, density_threshold, outfile_name):
    snap = pynbody.load(snap_name)
    gas = snap.gas
    filt = pynbody.filt.HighPass('rho', density_threshold)

    pos = gas[filt]['pos'].view(np.ndarray)
    data = dict(x=pos[:,0], y=pos[:,1], z=pos[:,2])
    print('output file', outfile_name)
    savemat(outfile_name, data)
    return pos

if __name__ == '__main__':
    snap_name = "../dataset/snapshot_0395"
    density_threshold = 6e-6
    convert_snapshot_to_mat(snap_name, density_threshold, 's395.mat')

    # import argparse
    # parser = argparse.ArgumentParser("Produce column density images")
    # parser.add_argument("-i", '--input', help='Gadget2 snapshot')
    # parser.add_argument("-c", '--center', help='Center snapshot on gas center of mass', action='store_true')
    # parser.add_argument("-w", '--width', help='Extent of the image in kpc', default=10, type=float)
    # parser.add_argument("-t", '--translate', help='Translate', default=None) # "0 -20 0"
    # parser.add_argument("-r", '--resolution', help='Pixels per side in image', default=200,type=int)
    # parser.add_argument("-p", '--pov', help='plane to print', choices=['xy', 'xz', 'zy'], default='xy')
    # parser.add_argument('--origin', help='Translate snap centering on this coordinates', required=False)
    # parser.add_argument('-d', "--folder", help='Folder where to save figures and data', default=None)
    # parser.add_argument("-o", '--output', help='The output image', default=None)
    # parser.add_argument("--dry", help='Just show the image', action='store_true')
