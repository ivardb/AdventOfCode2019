import collections
import sys
import time
import numpy as np
from matplotlib import pyplot as plt

from objects.computers.repairDrone import repairDrone


def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(",")]

def part1(data):
    grid = np.zeros((50, 50))
    position = (25, 25)
    computer = repairDrone(data, grid, position)
    try:
        computer.executeProgram()
    except IndexError:
        return bfs(grid, position)

def part2(data):
    grid = np.zeros((50, 50))
    position = (25, 25)
    computer = repairDrone(data, grid, position)
    try:
        computer.executeProgram()
    except IndexError:
        display(grid)
        time.sleep(2)
        target = [(iy,ix) for ix, row in enumerate(grid) for iy, i in enumerate(row) if i == 1][0]
        print(target)
        distances = bfs2(grid, target)
        return np.max(distances)

def display(grid):
    plt.figure()
    plt.imshow(grid)
    plt.show()

def bfs(grid, position):
    queue = collections.deque()
    queue.append(position)
    seen = set()
    seen.add(position)
    x = position[0]
    y = position[1]
    distances = np.zeros(grid.shape)
    while queue:
        current = queue.popleft()
        x = current[0]
        y = current[1]
        if grid[y, x] == 1:
            return distances[y, x]
        for newX, newY in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if grid[newY, newX] != 3 and (newX, newY) not in seen:
                seen.add((newX, newY))
                queue.append((newX, newY))
                distances[newY, newX] = distances[y, x] + 1
    return -1

def bfs2(grid, position):
    queue = collections.deque()
    queue.append(position)
    grid[position[1], position[0]] = 6
    distances = np.zeros(grid.shape)
    displayCount = 0
    while queue:
        displayCount+=1
        current = queue.popleft()
        if displayCount%10 == 0:
            display(grid)
        x = current[0]
        y = current[1]
        for newX, newY in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if grid[newY, newX] != 3 and grid[newY, newX] != 6:
                grid[newY, newX] = 6
                queue.append((newX, newY))
                distances[newY, newX] = distances[y, x] + 1
    return distances

data = readFile("../../data/day15.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day15.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()