from itertools import product
import math
import numpy as np
from PIL import Image
from datetime import datetime


class Piece:
    
    def __init__(self, label, color, move):
        self.label = label
        self.color = color
        self.move = move
        self.neighbors = Piece.calc_neighbors(move)
        
    @staticmethod
    def calc_neighbors(move):
        a, b = move
        avals = [-a, a]
        bvals = [-b, b]
        out = set()
        for pair in product(avals, bvals):
            out.add(pair)
        for pair in product(bvals, avals):
            out.add(pair)  
        return out


def spiral_to_xy(n):
    if n == 0:
        return (0, 0)
    # Determine the ring (R) 
    R = math.ceil((math.sqrt(n + 1) - 1) / 2)

    # corner vals to determine which side of the ring
    SW = 2 * R * (2 * R + 1)
    NW = 4 * R ** 2
    NE = 2 * R * (2 * R - 1)
    SE = (2 * R - 1)**2 - 1
    if n > SW:
        x = -R + n - SW
        y = -R
    elif n > NW:
        x = -R
        y = R - n + NW
    elif n > NE:
        x = R - n + NE
        y = R 
    else:
        x = R
        y = -R + n - SE
        
    return (x, y)


def xy_to_spiral(xy):
    x, y = xy
    if x == 0 and y == 0:
        return 0

    # Determine the ring (R) 
    R = max(abs(x), abs(y))

    # corner vals to determine which side of the ring
    SW = 2 * R * (2 * R + 1)
    NW = 4 * R ** 2
    NE = 2 * R * (2 * R - 1)
    SE = (2 * R - 1)**2 - 1
    if x == R and y > -R:
        n = SE + R + y
    elif y == R and x < R:
        n = NE - x + R
    elif x == -R and y < R:
        n = NW + R - y
    else:
        n = SW + R + x
        
    return n


# pieces = [
#     Piece('Black Alfil', [0, 0, 0], [2, 2]),
#     Piece('Gold Dromedary', [255, 215, 0], [0, 3]),
#     ]

# pieces = [
#     Piece('Black K', [0, 0, 0], [1, 2]),
#     Piece('Red K', [255, 0, 0], [1, 2]),
#     ]

# pieces = [
#     Piece('Wazir A', [145, 245, 172], [0, 1]),
#     Piece('Knight A', [145, 172, 245], [1, 2]),
#     Piece('Wazir B', [230, 129, 203], [0, 1]),
#     Piece('Knight B', [230, 203, 129], [1, 2]),
#     ]

# pieces = [
#     Piece('Black Zebra', [0, 0, 0], [2, 3]),
#     Piece('Red Dromedary', [255, 0, 0], [0, 3]),
#     Piece('Gold Alfil', [255, 215, 0], [2, 2]),
#     ]

# pieces = [
#     Piece('Red Dromedary', [255, 0, 0], [0, 3]),
#     Piece('Gold Alfil', [255, 215, 0], [2, 2]),
#     Piece('Black Zebra', [0, 0, 0], [2, 3]),
#     ]

pieces = [
    Piece('Gold Alfil', [249, 180, 25], [2, 2]),
    Piece('Olive Zebra', [91, 102, 33], [2, 3]),
    Piece('Orange Dromedary', [209, 125, 5], [0, 3]),
    ]

# pieces = [pieces[2], pieces[1], pieces[0]]
# pieces = [pieces[2], pieces[0], pieces[1]]
# pieces = [pieces[1], pieces[2], pieces[0]]
pieces = [pieces[1], pieces[0], pieces[2]]
# pieces = [pieces[0], pieces[2], pieces[1]]
# pieces = [pieces[0], pieces[1], pieces[2]]

dim = 299

file_name = f'{" - ".join([_.label for _ in pieces])} {dim}x{dim}.png'

seen = {_.label: set() for _ in pieces}
occupied = {_.label: set() for _ in pieces}
double_seen = set()

count = 0
target = dim**2
target_numbers = set(range(dim**2))
all_numbers = set(range((3 * dim)**2))

# base_color = [255, 255, 255] 
base_color = [244, 239, 233]

arr = np.array([[base_color for r in range(dim)] for c in range(dim)], 
               dtype=np.uint8)
shift = (dim - 1)//2

while True:
    current = pieces.pop(0)
    enemy_occupied = set()
    for enemy in pieces:
        enemy_occupied |= occupied[enemy.label]
    candidates = seen[current.label] | all_numbers
    chosen = min(candidates)
    occupied[current.label].add(chosen)
    target_numbers.discard(chosen)
    all_numbers.discard(chosen)
    seen[current.label].discard(chosen)
    coords = spiral_to_xy(chosen)
    x, y = coords
    
    row = dim - y - shift - 1
    col = x + shift
    
    if 0 <= row < dim and 0 <= col < dim:
    
        arr[row][col] = current.color

    for nbr in current.neighbors:
        tup = tuple([a + b for a, b in zip(nbr, coords)])
        new_seen = xy_to_spiral(tup)
        if (new_seen not in double_seen 
            and new_seen not in occupied[current.label]
            and new_seen not in enemy_occupied):
            seen[current.label].add(new_seen)
            # target_numbers.discard(new_seen)
            all_numbers.discard(new_seen)     
    for other in pieces:
        for dub in seen[current.label] & seen[other.label]:
           double_seen.add(dub) 
           seen[current.label].discard(dub)
           seen[other.label].discard(dub)
           target_numbers.discard(dub)
           
           
    pieces.append(current)
 
        
    count += 1
    
    # if count == 10:
    #     break
    
    if count % 1000 == 0:
        print(count, len(target_numbers), str(datetime.now()))
    # if count == 40:
    #     break


           
    if len(target_numbers) == 0:
        break


img = Image.fromarray(arr, 'RGB')
img.save(file_name)
print(file_name)