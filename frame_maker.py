

import numpy as np
from PIL import Image


def center_crop(nparr, dim):
    odim = nparr.shape[0]
    offset = (odim - dim) // 2
    out = nparr[offset: odim - offset, offset: odim - offset, :]
    return out

def magnify(nparr, factor):
    odim = nparr.shape[0]
    dim = odim * factor
    
    
    out = np.array([[[0, 0, 0] for r in range(dim)] for c in range(dim)], 
                   dtype=np.uint8)
    
    for i in range(odim):
        for j in range(odim):
            for k in range(factor):
                for l in range(factor):
                    
                    out[i * factor + k][j * factor + l] = nparr[i][j]
    
    
    return out


pfile = 'fast fiveleaper - thirteenleaper 405x405.pkl'


arr405 = np.load(pfile, allow_pickle=True)


arr5 = magnify(center_crop(arr405, 5), 81)
arr15 = magnify(center_crop(arr405, 15), 27)
arr45 = magnify(center_crop(arr405, 45), 9)
arr135 = magnify(center_crop(arr405, 135), 3)

img1 = Image.fromarray(arr5, 'RGB')
img1.save('frame_5_13_005.png')

img2 = Image.fromarray(arr15, 'RGB')
img2.save('frame_5_13_015.png')

img3 = Image.fromarray(arr45, 'RGB')
img3.save('frame_5_13_045.png')

img4 = Image.fromarray(arr135, 'RGB')
img4.save('frame_5_13_135.png')

img5 = Image.fromarray(arr405, 'RGB')
img5.save('frame_5_13_405.png')


