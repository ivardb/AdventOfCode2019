import sys
import numpy as np
import time

from objects.computers.simpleComputer import simpleComputer


def readFile(filename):
    with open(filename) as f:
        return np.asarray([int(x) for x in f.read().split(",")])

def part1(input):
    computer = simpleComputer(input)
    computer.executeProgram()
    return input[0]

def part2(input):
    for i in range(0, 100):
        for j in range(0, 100):
            updated = np.copy(input)
            updated[1] = i
            updated[2] = j
            try:
                answer = part1(updated)
            except IndexError:
                answer = 0
            if answer == 19690720:
                return 100 * i + j

input = readFile("../data/day2.txt")
input[1] = 12
input[2] = 2
start = time.time()
answer1 = part1(input)
end = time.time()
print("Part1:", answer1)
print("Duration:", end-start, "s")

input = readFile("../data/day2.txt")
start = time.time()
answer2 = part2(input)
end = time.time()
print("Part2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()

