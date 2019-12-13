import sys
import time

from objects.computers.BOOSTComputer import BOOSTComputer


def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]

def part1(data):
    computer = BOOSTComputer(data)
    computer.setInput(1)
    computer.executeProgram()


def part2(data):
    computer = BOOSTComputer(data)
    computer.setInput(2)
    computer.executeProgram()


data = readFile("../../data/day9.txt")
start = time.time()
part1(data)
end = time.time()
print("Duration:", end-start, "s")

data = readFile("../../data/day9.txt")
start = time.time()
part2(data)
end = time.time()
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()