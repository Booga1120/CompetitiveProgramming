import sys
import math

def canDistribute(area, pieradii, numfriends):
    count = 0
    for pie in pieradii:
        count += int(pie / area)
        if count >= numfriends:
            return True
    return False

def main():
    testcases = int(sys.stdin.readline())

    for _ in range(testcases):
        input = list(map(int,sys.stdin.readline().split()))
        numpies = input[0]
        numfriends = input[1]
        pieradii = list(map(int,sys.stdin.readline().split()))
        for i in range(len(pieradii)):
            pieradii[i] = math.pi * pieradii[i] * pieradii[i]
        pieradii.sort(reverse=True)
        maxarea = pieradii[0]
        minarea = 0

        while maxarea - minarea > 0.0001:
            mid = (minarea + maxarea) / 2
            if canDistribute(mid, pieradii, numfriends + 1):
                minarea = mid
            else:
                maxarea = mid
        
        print(maxarea)

if __name__ == "__main__":
    main()