# 1-dimensional cellular automaton with png output
# 1: ooo    xoo 5
# 2: oox     ooo 1
# 3: oxx      oox 2
# 4: oxo       oxo 4
# 5: xoo        xox 6
# 6: xox         oxx 3
# 7: xxx          xxx 7
# 8: xxo           xxo 8
# synthese: xoooxoxxxo
# to do:
# Regeln u Reihenfolge (8bit) pruefen

import random
import png

width = 2001
depth = 1000
cell_grid = [["0"]*width]

neighbors = [""]*8
rules = [[""]*8]*256

alphabet = ["0","1"]
rand_str = lambda n: "".join([random.choice(alphabet) for i in range(width)])

def remove_0b(binary):
    binary = binary[2:len(binary)]
    return binary

# possible neighbors
for i in range(8):
    neighbors[7-i] = remove_0b(str(bin(i))).zfill(3)
# new version
for i in range(256):
    rules[i] = remove_0b(str(bin(i))).zfill(8)

starting_condition = rand_str(width)

def evolve(row,n):
    new_row = [""]*width
    cells = [row[len(row)-1]]+row+[row[0]]
    for i in range(len(cells)-2):
        found = neighbors.index(cells[i]+cells[i+1]+cells[i+2])
        new_row[i] = rules[n][found]
    return new_row

def convert(strings):
    int_list = [[0]*len(strings[i]) for i in range(len(strings))]
    for s in range(len(strings)-1):
        for c in range(len(strings[s])-1):
            int_list[s][c] = 255*int(strings[s][c])
    return int_list

def output(array,filename):
    image = open("./img/%s.png"%(filename),"wb")
    w = png.Writer(width,depth,greyscale=True)
    w.write(image, convert(array))

#for n in range(256):
#    cell_grid = [starting_condition]
#    for i in range(depth-1): cell_grid.append(evolve(cell_grid[i],n))
#    output(cell_grid,str(n).zfill(3))

cell_grid[0][1000] = "1"
for i in range(depth-1): cell_grid.append(evolve(cell_grid[i],30))
output(cell_grid,"rule_30")
