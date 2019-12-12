import numpy as np
import sys
import math
import time

def readFile(filename):
    with open(filename) as f:
        input = [int(x) for x in f]
    return np.asarray(input)


def part1(input):
    return np.sum(np.floor(input/3)-2)


def part2(input):
    output = np.floor(input/3)-2
    return np.sum([calcMass(x) for x in output])


def calcMass(x):
    fuel = math.floor(x/3)-2
    if fuel > 0:
        return x + calcMass(fuel)
    return x


input = readFile("../data/day1.txt")
start = time.time()
answer1 = part1(input)
end = time.time()
print("Part1:", answer1)
print("Duration:", end-start, "s")

input = readFile("../data/day1.txt")
start = time.time()
answer2 = part2(input)
end = time.time()
print("Part2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()
