import sys
import time
import numpy as np

relativeBase = 0
position = 0
inputCode = 0

def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]


def part1(data):
    global inputCode
    inputCode = 1
    global position
    position = 0
    global relativeBase
    relativeBase = 0
    data = np.pad(data, (0,100), mode='constant', constant_values=0)
    data = data.astype(np.int64)
    while True:
        advance = processCode(data, position)
        if advance == -1:
            break
        else:
            position+=advance


def part2(data):
    global inputCode
    inputCode = 2
    global position
    position = 0
    global relativeBase
    relativeBase = 0
    data = np.pad(data, (0,10000), mode='constant', constant_values=0)
    data = data.astype(np.int64)
    while True:
        advance = processCode(data, position)
        if advance == -1:
            break
        else:
            position+=advance

def processCode(data, pos):
    global position
    global relativeBase
    global inputCode
    instruction = data[pos]
    A = int(instruction/10000)
    instruction -= A * 10000
    B = int(instruction/1000)
    instruction -= B * 1000
    C = int(instruction/100)
    instruction -= C * 100
    opcode = instruction
    if opcode == 1:
        val1 = getParameter(data, pos+1, C)
        val2 = getParameter(data, pos+2, B)
        if A==2:
            output = data[pos+3]+relativeBase
        else:
            output = data[pos+3]
        data[output] = val1 + val2
        return 4
    elif opcode == 2:
        val1 = getParameter(data, pos+1, C)
        val2 = getParameter(data, pos+2, B)
        if A==2:
            output = data[pos+3]+relativeBase
        else:
            output = data[pos+3]
        data[output] = val1 * val2
        return 4
    elif opcode == 3:
        if C==1:
            data[data[pos + 1]] = inputCode
        else:
            data[data[pos+1]+relativeBase] = inputCode
        return 2
    elif opcode == 4:
        par1 = data[pos + 1]
        if C == 0:
            outputProgram = data[par1]
        elif C==1:
            outputProgram = par1
        else:
            outputProgram = data[relativeBase+par1]
        print(outputProgram)
        return 2
    elif opcode == 5:
        val1 = getParameter(data, pos+1, C)
        val2 = getParameter(data, pos+2, B)
        if val1!=0:
            position = val2
            return 0
        else:
            return 3
    elif opcode == 6:
        val1 = getParameter(data, pos+1, C)
        val2 = getParameter(data, pos+2, B)
        if val1==0:
            position = val2
            return 0
        else:
            return 3
    elif opcode == 7:
        val1 = getParameter(data, pos+1, C)
        val2 = getParameter(data, pos+2, B)
        if A==2:
            output = data[pos+3]+relativeBase
        else:
            output = data[pos+3]
        if val1<val2:
            data[output] = 1
        else:
            data[output] = 0
        return 4
    elif opcode == 8:
        val1 = getParameter(data, pos+1, C)
        val2 = getParameter(data, pos+2, B)
        if A==2:
            output = data[pos+3]+relativeBase
        else:
            output = data[pos+3]
        if val1==val2:
            data[output] = 1
        else:
            data[output] = 0
        return 4
    elif opcode == 9:
        val1 = getParameter(data, pos+1, C)
        relativeBase+=val1
        return 2
    elif opcode == 99:
        return -1

def getParameter(data, pos, type):
    global relativeBase
    if type==0:
        return data[data[pos]]
    if type==1:
        return data[pos]
    if type==2:
        return data[relativeBase+data[pos]]


data = readFile("../data/day9.txt")
start = time.time()
part1(data)
end = time.time()
print("Duration:", end-start, "s")

data = readFile("../data/day9.txt")
start = time.time()
part2(data)
end = time.time()
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()