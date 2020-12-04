import sys
import time
import numpy as np

def readFile(filename):
    with open(filename) as f:
        data = [int(x.strip()) for x in f.read()]
        return data


def part1(data):
    input = data
    for phase in range(100):
        output = np.zeros(len(input))
        for i in range(len(output)):
            multiplier = getMultiplier(i+1, len(output))
            sum = np.sum(input*multiplier)
            output[i] = (abs(sum)%10)
        input = output
    return "".join([str(int(x)) for x in input[:8]])


def part2(data):
    offset = int("".join(map(str, data[:7])))
    input = data * 10000
    input = input[offset:]
    for phase in range(100):
        output = np.zeros(len(input))
        s = np.sum(input)
        for i in range(len(output)):
            output[i] = ((s % 10) + 10) % 10
            s -= input[i]
        input = output
    return "".join([str(int(x)) for x in input[:8]])


def getMultiplier(it, n):
    basePattern = [0, 1, 0, -1]
    output = np.zeros(n)
    currentIndex = 0
    currentIt = 1
    for i in range(n):
        if currentIt>=it:
            currentIt=0
            currentIndex = (currentIndex+1)%4
        output[i] = basePattern[currentIndex]
        currentIt+=1
    return output

def part22(data):
    offset = int("".join(map(str, data[:7])))
    input = data * 10000
    input = input[offset:]
    for phase in range(100):
        output = np.cumsum(input[::-1]) % 10
        input = output[::-1]
    return "".join([str(int(x)) for x in input[:8]])


data = readFile("../../data/day16.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day16.txt")
start = time.time()
answer2 = part22(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()
