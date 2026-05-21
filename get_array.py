from PIL import Image

import numpy as np
import copy


def get_colors(nparr):
    colors = set()
    
    for row in nparr:
        for color in row:
            colors.add(tuple(color))
            
    return colors
    
def color_swap(nparr, cmap):
    new = copy.deepcopy(nparr)
    
    rows, cols, depth = new.shape
    
    for row in range(rows):
        for col in range(cols):
            new[row][col] = cmap[tuple(nparr[row][col])]
            
    return new
    


fp_in = "Gold Alfil - Olive Zebra - Orange Dromedary 299x299.png"
img = Image.open(fp_in) 
arr = np.array(img)

colors = get_colors(arr)

# color_map = {(np.uint8(91), np.uint8(102), np.uint8(33)): 
#                [np.uint8(13), np.uint8(13), np.uint8(21)],
#              (np.uint8(209), np.uint8(125), np.uint8(5)):
#                [np.uint8(241), np.uint8(155), np.uint8(42)],
#              (np.uint8(249), np.uint8(180), np.uint8(25)):
#                [np.uint8(149), np.uint8(29), np.uint8(241)],
#              (np.uint8(244), np.uint8(239), np.uint8(233)): 
#                [np.uint8(191), np.uint8(240), np.uint8(52)]}
    
color_map = {(np.uint8(91), np.uint8(102), np.uint8(33)): 
               [np.uint8(191), np.uint8(240), np.uint8(52)],
             (np.uint8(209), np.uint8(125), np.uint8(5)):
               [np.uint8(241), np.uint8(155), np.uint8(42)],
             (np.uint8(249), np.uint8(180), np.uint8(25)):
               [np.uint8(149), np.uint8(29), np.uint8(241)],
             (np.uint8(244), np.uint8(239), np.uint8(233)): 
               [np.uint8(13), np.uint8(13), np.uint8(21)]}
    
    
color_map = {(np.uint8(91), np.uint8(102), np.uint8(33)): 
               [np.uint8(191), np.uint8(240), np.uint8(52)],
             (np.uint8(209), np.uint8(125), np.uint8(5)):
               [np.uint8(241), np.uint8(155), np.uint8(42)],
             (np.uint8(249), np.uint8(180), np.uint8(25)):
               [np.uint8(13), np.uint8(13), np.uint8(21)],
             (np.uint8(244), np.uint8(239), np.uint8(233)): 
               [np.uint8(149), np.uint8(29), np.uint8(241)]}
    
new_arr = color_swap(arr, color_map)
out_img = Image.fromarray(new_arr, 'RGB')