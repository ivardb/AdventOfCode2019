import sys
import time

from objects.computers.TESTComputer import TESTComputer

def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]

def part1(data):
    computer = TESTComputer(data)
    computer.setInput(1)
    computer.executeProgram()


def part2(data):
    computer = TESTComputer(data)
    computer.setInput(5)
    computer.executeProgram()

data = readFile("../../data/day5.txt")
start = time.time()
part1(data)
end = time.time()
print("Duration:", end-start, "s")

data = readFile("../../data/day5.txt")
start = time.time()
part2(data)
end = time.time()
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()
