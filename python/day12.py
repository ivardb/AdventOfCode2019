import sys
import time
from objects.moon import *
import numpy as np
from sympy import lcm

def readFile(filename):
    with open(filename) as f:
        return [moon(line.strip()) for line in f.readlines()]

def part1(data):
    for i in range(1000):
        applyGravity(data)
        applyVelocity(data)
    return np.sum([moon.kinetic()*moon.potential() for moon in data])


def part2(data):
    counterX, counterY, counterZ = 1,1,1
    addX, addY, addZ = True, True, True
    while addX or addY or addZ:
        applyGravity(data)
        applyVelocity(data)
        x = tuple(moon.dx for moon in data)
        y = tuple(moon.dy for moon in data)
        z = tuple(moon.dz for moon in data)
        if addX and x!=(0,0,0,0):
            counterX+=1
        else:
            addX = False

        if addY and y!=(0,0,0,0):
            counterY += 1
        else:
            addY = False

        if addZ and z!=(0,0,0,0):
            counterZ += 1
        else:
            addZ = False
    return lcm([counterZ*2, counterX*2, counterY*2])


def applyGravity(data):
    for i in range(len(data)-1):
        for j in range(i, len(data)):
            moon = data[i]
            moon2 = data[j]
            updateVelocity(moon, moon2)

def updateVelocity(m1, m2):
    if m1.x>m2.x:
        m1.dx += -1
        m2.dx += 1
    elif m1.x<m2.x:
        m1.dx += 1
        m2.dx += -1

    if m1.y>m2.y:
        m1.dy += -1
        m2.dy += 1
    elif m1.y<m2.y:
        m1.dy += 1
        m2.dy += -1

    if m1.z>m2.z:
        m1.dz += -1
        m2.dz += 1
    elif m1.z<m2.z:
        m1.dz += 1
        m2.dz += -1

def applyVelocity(data):
    for moon in data:
        moon.applyVelocity()


data = readFile("../data/day12.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../data/day12.txt")
#data = readFile("../data/test.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()
