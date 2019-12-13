import sys
import time
import numpy as np

from objects.computers.arcadeCabinet import arcadeCabinet


def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]


def part1(data):
    grid = np.zeros((50, 50))
    computer = arcadeCabinet(data, grid)
    computer.executeProgram()
    return len(np.where(grid==2)[0])


def part2(data):
    grid = np.zeros((50, 50))
    data[0] = 2
    computer = arcadeCabinet(data, grid)
    computer.executeProgram()
    return computer.score

data = readFile("../../data/day13.txt")
#data = readFile("../../data/test.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day13.txt")
#data = readFile("../../data/test.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()