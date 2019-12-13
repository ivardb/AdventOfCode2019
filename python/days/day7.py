import sys
import time
import numpy as np
import itertools
from objects.amplifier import *

position = 0
outputProgram = 0


def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]

def part1(data):
    phaseSettings = itertools.permutations(range(5))
    max = 0
    global outputProgram
    for setting in phaseSettings:
        outputProgram = 0
        for phase in setting:
            inputCode = phase
            program = np.copy(data)
            global position
            position = 0
            while True:
                advance = processCode(program, position, inputCode)
                inputCode = outputProgram
                if advance == -1:
                    #finish program
                    break
                else:
                    position+=advance
        if outputProgram>max:
            max=outputProgram
    return max

def part2(data):
    phaseSettings = itertools.permutations(range(5,10))
    max = 0
    for setting in phaseSettings:
        amps = list()
        for phase, name in zip(setting, "ABCDE"):
            amps.append(amplifier(np.copy(data), phase, name))
        amps[0].next = amps[1]
        amps[1].next = amps[2]
        amps[2].next = amps[3]
        amps[3].next = amps[4]
        amps[4].next = amps[0]
        amps[0].input = 0
        amps[0].process()
        output = amps[0].input
        if output > max:
            max = output
    return max

def processCode(data, pos, inputCode):
    global position
    global outputProgram
    instruction = data[pos]
    A = int(instruction/10000)
    instruction -= A * 10000
    B = int(instruction/1000)
    instruction -= B * 1000
    C = int(instruction/100)
    instruction -= C * 100
    opcode = instruction
    if opcode == 1:
        if C == 0:
            val1 = data[data[pos + 1]]
        else:
            val1 = data[pos + 1]
        if B == 0:
            val2 = data[data[pos + 2]]
        else:
            val2 = data[pos + 2]
        output = data[pos + 3]
        data[output] = val1 + val2
        return 4
    elif opcode == 2:
        if C == 0:
            val1 = data[data[pos + 1]]
        else:
            val1 = data[pos + 1]
        if B == 0:
            val2 = data[data[pos + 2]]
        else:
            val2 = data[pos + 2]
        output = data[pos + 3]
        data[output] = val1 * val2
        return 4
    elif opcode == 3:
        data[data[pos + 1]] = inputCode
        return 2
    elif opcode == 4:
        par1 = data[pos + 1]
        if C == 0:
            outputProgram = data[par1]
        else:
            outputProgram = par1
        return 2
    elif opcode == 5:
        if C == 0:
            val1 = data[data[pos + 1]]
        else:
            val1 = data[pos + 1]
        if B == 0:
            val2 = data[data[pos + 2]]
        else:
            val2 = data[pos + 2]
        if val1!=0:
            position = val2
            return 0
        else:
            return 3
    elif opcode == 6:
        if C == 0:
            val1 = data[data[pos + 1]]
        else:
            val1 = data[pos + 1]
        if B == 0:
            val2 = data[data[pos + 2]]
        else:
            val2 = data[pos + 2]
        if val1==0:
            position = val2
            return 0
        else:
            return 3
    elif opcode == 7:
        if C == 0:
            val1 = data[data[pos + 1]]
        else:
            val1 = data[pos + 1]
        if B == 0:
            val2 = data[data[pos + 2]]
        else:
            val2 = data[pos + 2]
        output = data[pos+3]
        if val1<val2:
            data[output] = 1
        else:
            data[output] = 0
        return 4
    elif opcode == 8:
        if C == 0:
            val1 = data[data[pos + 1]]
        else:
            val1 = data[pos + 1]
        if B == 0:
            val2 = data[data[pos + 2]]
        else:
            val2 = data[pos + 2]
        output = data[pos+3]
        if val1==val2:
            data[output] = 1
        else:
            data[output] = 0
        return 4
    elif opcode == 99:
        return -1

data = readFile("../../data/day7.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day7.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()