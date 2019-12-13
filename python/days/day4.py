import sys
import time

def part1(numbers):
    count = 0
    for number in numbers:
        n = str(number)
        old = n[0]
        increasing = True
        same = False
        for i in range(1,len(n)):
            if n[i]<old:
                increasing=False
                break
            if n[i] == old:
                same = True
            old = n[i]
        if same and increasing:
            count += 1
    return count

def part2(numbers):
    count = 0
    for number in numbers:
        n = str(number)
        old = n[0]
        repeatCount = 1
        counts = list()
        increasing = True
        for i in range(1, len(n)):
            if n[i]<old:
                increasing=False
                break
            if n[i] == old:
                repeatCount += 1
            else:
                counts.append(repeatCount)
                repeatCount=1
            old = n[i]
        counts.append(repeatCount)
        if 2 in counts and increasing:
            count += 1
    return count

input = range(137683, 596253)
start = time.time()
answer1 = part1(input)
end = time.time()
print("Part1:", answer1)
print("Duration:", end-start, "s")

input = range(137683, 596253)
start = time.time()
answer2 = part2(input)
end = time.time()
print("Part2:", answer2)
print("Duration:", end-start, "s")
if __name__ == "__main__":
    sys.exit()