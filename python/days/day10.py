import time
import sys
import numpy as np
from math import *


def readFile(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f]
        data = np.empty((len(lines), len(lines[0])), dtype=np.object)
        for index, line in enumerate(lines):
            data[index,:] = [x for x in line]
        return data

def part1(data):
    max = 0
    maxY = 0
    maxX = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x,y] == '#':
                count = countAsteroids(data, x, y)
                if count > max:
                    max = count
                    maxX = x
                    maxY = y
    return max


def part2(data):
    x = 29
    y = 28
    count = 0
    validDir = list()
    for dx in range(-x, len(data)-x):
        for dy in range(-y, len(data[0])-y):
            if valid(dx, dy):
                validDir.append((dx, dy))
    sortedDir = sorted(validDir, key=lambda dir: atan2(dir[1],dir[0])/pi*180+180, reverse=True)
    i = 0
    while count<199:
        direction = sortedDir[i]
        xHit, yHit = findHit(data, x, y, direction)
        if xHit != -1:
            count+=1
            data[xHit, yHit] = '.'
        i += 1
    while True:
        direction = sortedDir[i]
        xHit, yHit = findHit(data, x, y, direction)
        if xHit != -1:
            return yHit*100+xHit
        i += 1


def findHit(data, x, y, direction):
    dx = direction[0]
    dy = direction[1]
    newX = x
    newY = y
    newX += dx
    newY += dy
    while 0 <= newX < len(data) and 0 <= newY < len(data[0]):
        value = data[newX,newY]
        if value == '#':
            return newX, newY
        newX += dx
        newY += dy
    return -1, -1

def countAsteroids(data, x, y):
    count = 0
    for dx in range(-x, len(data)-x):
        for dy in range(-y, len(data[0])-y):
            if not valid(dx,dy):
                continue
            newX = x
            newY = y
            newX += dx
            newY += dy
            while 0 <= newX < len(data) and 0 <= newY < len(data[0]):
                value = data[newX,newY]
                if value == '#':
                    count+=1
                    break
                newX += dx
                newY += dy
    return count

def valid(dx, dy):
    if dx == 0:
        if abs(dy) != 1:
            return False
    if dy ==0:
        if abs(dx) != 1:
            return False
    for div in range(2, min(abs(dx),abs(dy))+1):
        if dx%div==0 and dy%div==0:
            return False
    return True

data = readFile("../../data/day10.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day10.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()