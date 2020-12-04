import sys
import time
import numpy as np

from objects.computers.ASCII import ASCII


def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]


def part1(data):
    grid = np.empty((41, 45), dtype=object)
    computer = ASCII(data, grid)
    computer.executeProgram()
    computer.displayGrid()
    intersections = list()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == '#':
                intersection = True
                for newX, newY in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                    if grid.shape[1] > newX > 0 and grid.shape[0] > newY > 0:
                        if grid[newY, newX] != '#':
                            intersection = False
                            break
                    else:
                        intersection = False
                        break;
                if intersection:
                    intersections.append((x,y))
    return np.sum([x*y for x,y in intersections])

def part2(data):
    pass


data = readFile("../../data/day17.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day17.txt")
start = time.time()
part2(data)
end = time.time()
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()