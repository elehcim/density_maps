import os
import numpy as np
import matplotlib.pyplot as plt
import pynbody

def produce_image(snap_name, pov, center, width, resolution, shift, output, dry, np_out, boxsize=100):
    s = pynbody.load(snap_name)
    pynbody.analysis.halo.transformation.translate(s, [-boxsize/2]*3)
    if center:
        pynbody.analysis.halo.center(s.g)
    elif shift is not None:
        translation = np.array(list(map(float,shift.split())))
        print("translating of ", translation)
        pynbody.analysis.halo.transformation.translate(s.g, translation)

    if pov == 'xy':
        im = pynbody.plot.sph.image(s.g, qty='rho', units="Msol pc**-2", width=width, resolution=resolution)
    elif pov == 'xz':
        s.g.rotate_x(-90)
        im = pynbody.plot.sph.image(s.g, qty='rho', units="Msol pc**-2", width=width, resolution=resolution)
        plt.gca().set_ylabel('z/kpc')
    elif pov == 'zy':
        s.g.rotate_y(90)
        im = pynbody.plot.sph.image(s.g, qty='rho', units="Msol pc**-2", width=width, resolution=resolution)
        plt.gca().set_xlabel('z/kpc')
    if dry:
        plt.show()
        return 
    plt.savefig(output, dpi=300)
    if np_out:
        np.save(np_out, im)
    return im

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Produce column density images")
    parser.add_argument("-i", '--input', help='Gadget2 snapshot')
    parser.add_argument("-c", '--center', help='Center snapshot on gas center of mass', action='store_true')
    parser.add_argument("-w", '--width', help='Extent of the image in kpc', default=10, type=float)
    parser.add_argument("-t", '--translate', help='Translate', default=None) # "0 -20 0"
    parser.add_argument("-r", '--resolution', help='Pixels per side in image', default=200,type=int)
    parser.add_argument("-p", '--pov', help='plane to print', choices=['xy', 'xz', 'zy'], default='xy')
    parser.add_argument('--origin', help='Translate snap centering on this coordinates', required=False)
    parser.add_argument('-d', "--folder", help='Folder where to save figures and data', default=None)
    parser.add_argument("-o", '--output', help='The output image', default=None)
    parser.add_argument("--dry", help='Just show the image', action='store_true')

    args = parser.parse_args()
    np_out=None
    if args.folder is not None:
        os.makedirs(args.folder, exist_ok=True)
        args.output = os.path.join(args.folder, os.path.basename(args.input)+".jpg")
        np_out = os.path.join(args.folder, os.path.basename(args.input))
    elif args.output is None:
        args.output = args.input+".jpg"
        np_out = args.input + ".npy"
    else:
        np_out = os.path.splitext(args.output)[0] + '.npy'
    im = produce_image(args.input, args.pov, args.center, args.width, 
                       args.resolution, args.translate, args.output, args.dry, np_out)

# pynbody.analysis.halo.transformation.translate