import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000000)
    balls, paddles = map(int, sys.stdin.readline().split())

    orientations = [('L', 0, 0)]*paddles
    for paddle in range(paddles):
        isLeft, leftnum, rightnum = sys.stdin.readline().split()
        orientations[paddle] = (isLeft, int(leftnum)-1, int(rightnum)-1)
    
    def flip(switch, b):
        if switch == -1 or b == 0:
            return
        current = orientations[switch]
        if current[0] == 'L':
            if b % 2 == 1:
                orientations[switch] = ('R', current[1], current[2])
                flip(current[1], b//2 + 1)
            else:
                flip(current[1], b//2)
            flip(current[2], b//2)
        else:
            if b % 2 == 1:
                orientations[switch] = ('L', current[1], current[2])
                flip(current[2], b//2 + 1)
            else:
                flip(current[2], b//2)
            flip(current[1], b//2)
    
    flip(0, balls)

    print(''.join(orientation[0] for orientation in orientations))

if __name__ == "__main__":
    main()