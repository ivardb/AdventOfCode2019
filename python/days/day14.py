import sys
import time
import math

from objects.chemical import chemical


def readFile(filename):
    data = dict()
    data["ORE"] = chemical("ORE", data)
    with open(filename) as f:
        for line in [x.strip() for x in f.readlines()]:
            ioSplit = line.split(" => ")
            output = ioSplit[1].strip()
            input = ioSplit[0].strip()
            outputSplit = output.split(" ")
            outputAmount = outputSplit[0]
            outputName = outputSplit[1]

            outputObject = data.get(outputName, None)
            if outputObject is None:
                newObject = chemical(outputName, data)
                outputObject = newObject
                data[outputName] = newObject
            outputObject.createdQuantity = int(outputAmount)

            for ingredient in [x.strip() for x in input.split(",")]:
                ingSplit = ingredient.split(" ")
                ingAmount = int(ingSplit[0])
                ingName = ingSplit[1]
                outputObject.addIngredient(ingName, ingAmount)
        return data



def part1(data):
    return data.get("FUEL").getComponent(1)


def part2(data):
    return search(data, 1000000000000, math.floor(1000000000000/data.get("FUEL").getComponent(1)), 100000000)


def search(data, amount, start, end):
    cleanData(data)
    if start>=(end-1):
        if data.get("FUEL").getComponent(start)>amount:
            return start-1
        return start
    middle = int((start+end)/2)
    ore = data.get("FUEL").getComponent(middle)
    if ore > amount:
        return search(data, amount, start, middle)
    if ore == amount:
        return middle
    if ore < amount:
        return search(data, amount, middle, end)

def cleanData(data):
    for chem in data.values():
        chem.stored = 0



data = readFile("../../data/day14.txt")
start = time.time()
answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../../data/day14.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()