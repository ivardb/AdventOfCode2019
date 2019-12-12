import sys
import time

def readFile(filename):
    with open(filename) as f:
        data = [x.strip() for x in f]
    return data


def part1(data):
    orbits = {}
    for orbit in data:
        split = orbit.split(")")
        orbits[split[1]] = split[0]
    count = 0
    for planet in orbits.keys():
        value = orbits.get(planet)
        count+=1
        while value != "COM":
            value = orbits.get(value)
            count+=1
    return count


def part2(data):
    orbits = {}
    for orbit in data:
        split = orbit.split(")")
        orbits[split[1]] = split[0]
    YouOrbitPath = list()
    value = orbits.get("YOU")
    YouOrbitPath.append(value)
    while value != "COM":
        value = orbits.get(value)
        YouOrbitPath.append(value)

    SANOrbit = list()
    value = orbits.get("SAN")
    SANOrbit.append(value)
    while value != "COM":
        value = orbits.get(value)
        SANOrbit.append(value)
    commonPoint = [x for x in YouOrbitPath if x in SANOrbit][0]
    return YouOrbitPath.index(commonPoint)+SANOrbit.index(commonPoint)

data = readFile("../data/day6.txt")
start = time.time()

answer1 = part1(data)
end = time.time()
print("Part 1:", answer1)
print("Duration:", end-start, "s")

data = readFile("../data/day6.txt")
start = time.time()
answer2 = part2(data)
end = time.time()
print("Part 2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()