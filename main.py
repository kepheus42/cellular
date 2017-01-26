# 1-dimensional cellular automaton
# 1: ooo    xoo 5
# 2: oox     ooo 1
# 3: oxx      oox 2
# 4: oxo       oxo 4
# 5: xoo        xox 6
# 6: xox         oxx 3
# 7: xxx          xxx 7
# 8: xxo           xxo 8
# synthese: xoooxoxxxo
#

import random
import png

width = 1000
depth = 1000
cell_grid = [""]

alphabet = ["0","1"]
rand_str = lambda n: "".join([random.choice(alphabet) for i in range(width)])

def remove_0b(binary):
    binary = binary[2:len(binary)]
    return binary

rule = ["1000101110"]
for i in range(256): rule = rule + [remove_0b(str(bin(i))).zfill(8)]

starting_condition = rand_str(width)

def evolve(cell,n):
    new = ""
    cells = cell[len(cell)-1]+cell+cell[0]
    for i in range(len(cells)-2):
        found = rule[0].index(cells[i:i+3])
        new = new+rule[n][found]
    return new

#Text output
#for n in range(256):
#    cell_grid = [starting_condition]
#    for i in range(depth-1): cell_grid.append(evolve(cell_grid[i],n))
#    f = open("cellular-rule-%s"%(str(n).zfill(3)), "w")
#    for s in cell_grid: f.write(s+"\n")

for n in range(256):
    cell_grid = [starting_condition]
    for i in range(depth-1): cell_grid.append(evolve(cell_grid[i],n))
    image = open("./img/%s.png"%(str(n).zfill(3)),"wb")
    w = png.Writer(1000,1000,greyscale=True)
    w.write(image, cell_grid)
#
#    for s in cell_grid: f.write(s+"\n")
