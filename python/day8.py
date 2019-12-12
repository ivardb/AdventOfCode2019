import sys
import time
import numpy as np
from matplotlib import pyplot as plt

def readFile(filename):
    with open(filename) as f:
        data = [int(x.strip()) for x in f.read()]
        return np.asarray(data)

def part1(data):
    width = 25
    height = 6
    index = 0
    minimum = 25*6
    answer = 0
    while index<len(data):
        imageLayer = np.zeros((6*25))
        iIndex = 0
        for h in range(height):
            for w in range(width):
                imageLayer[iIndex] = data[index]
                index+=1
                iIndex += 1
        count = len(np.where(imageLayer==0)[0])
        if count < minimum:
            minimum = count
            oneCount = len(np.where(imageLayer==1)[0])
            twoCount = len(np.where(imageLayer==2)[0])
            answer = oneCount*twoCount
    return answer

def part2(data):
    width = 25
    height = 6
    index = 0
    layerCount = int(len(data)/(width*height))
    layers = np.zeros((height, width, layerCount))
    for l in range(layerCount):
        for h in range(height):
            for w in range(width):
                layers[h,w,l] = data[index]
                index += 1
    image = np.zeros((height, width))
    for h in range(height):
        for w in range(width):
            nonZeroIndex = np.where(layers[h,w,:]!=2)[0][0]
            image[h,w] = layers[h,w,nonZeroIndex]
    plt.figure()
    plt.imshow(image, cmap="gray")
    plt.show()

data = readFile("../data/day8.txt")
print(len(data)/(25*6))
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../data/day8.txt")
start = time.time()
part2(data)
end = time.time()
print("Part 2:")
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()