import sys
import time
import numpy as np
from objects.robot import *
from matplotlib import pyplot as plt

def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]


def part1(data):
    grid = dict()
    data = np.pad(data, (0,1000), mode='constant', constant_values=0)
    data = data.astype(np.int64)
    bot = robot(grid, (250, 250), data)
    bot.executeProgram()
    return len(bot.getPainted())


def part2(data):
    grid = dict()
    data = np.pad(data, (0,1000), mode='constant', constant_values=0)
    data = data.astype(np.int64)
    bot = robot(grid, (0, 0), data)
    bot.grid[bot.gridPosition] = 1
    bot.executeProgram()
    keys = bot.grid.keys()
    maxX = np.max([x for x,y in keys])
    maxY = np.max([y for x,y in keys])
    image = np.zeros((maxX+1, maxY+1))
    for key in keys:
        value = bot.grid.get(key)
        image[key[0], key[1]] = value
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.show()


data = readFile("../data/day11.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../data/day11.txt")
start = time.time()
part2(data)
end = time.time()
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()