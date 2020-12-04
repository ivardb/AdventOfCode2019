import sys
import numpy as np
import days.config as c

def readFile(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]
        data = np.empty((len(lines), len(lines[0])), dtype=object)
        for index, line in enumerate(lines):
            data[index,:] = [x.strip() for x in line]
        return data


def part1(data):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i,j].islower():
                c.amountOfKeys+=1
    numpyThing = np.where(data=='@')
    startPosition = (numpyThing[1][0], numpyThing[0][0])
    #construct tree, with children being all next possibilities with updated distance.
    root = Tree(data, 0, startPosition, set(), set())
    root.createChildren()
    return c.minimum

def addMinima(distance):
    c.minimum = min(c.minimum, distance)

if __name__ == "__main__":
    from objects.tree import Tree
    amountOfKeys = 0
    minimum = 100000000
    #data = readFile("../../data/test.txt")
    data = readFile("../../data/day18.txt")
    answer1 = part1(data)
    print(answer1)
    sys.exit()