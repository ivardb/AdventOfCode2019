import time
import sys

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def readFile(filename):
    with open(filename) as f:
        A, B = f.read().split("\n")
        A, B = [x.split(',') for x in [A,B]]
        return A, B

def part1(A, B):
    points1 = getPoints(A).keys()
    points2 = getPoints(B).keys()
    intersection = points1&points2
    return min([abs(x)+abs(y) for x,y in intersection])


def part2(A, B):
    points1 = getPoints(A)
    points2 = getPoints(B)
    intersection = points1.keys() & points2.keys()
    return min([points1[coord]+points2[coord] for coord in intersection])


def getPoints(input):
    x = 0
    y = 0
    res = {}
    length = 0
    for move in input:
        direction = move[0]
        dist = int(move[1:])
        for i in range(dist):
            length+=1
            x += DX[direction]
            y += DY[direction]
            if (x,y) not in res:
                res[(x,y)] = length
    return res

A, B = readFile("../../data/day3.txt")
start = time.time()
answer1 = part1(A, B)
end = time.time()
print("Part1:", answer1)
print("Duration:", end-start, "s")

A, B = readFile("../../data/day3.txt")
start = time.time()
answer2 = part2(A, B)
end = time.time()
print("Part2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()