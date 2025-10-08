import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000)
    papers = int(sys.stdin.readline().strip())
    cites = []
    for i in range(papers):
        papercites = int(sys.stdin.readline().strip())
        cites.append(papercites)
    cites.sort()

    def checkValid(num):
        idx = 0
        while idx < len(cites) and cites[idx] < num:
            idx += 1
        if idx >= len(cites):
            return False
        if len(cites) - idx >= num:
            return True
        else:
            return False
    
    lower = 0
    upper = papers
    found = False
    while not found:
        middle = int((lower + upper) / 2)
        if upper - lower <= 1:
            found = True
            break
        if checkValid(middle):
            lower = middle
        else:
            upper = middle
    if checkValid(upper):
        print(upper)
    else:
        print(lower)

if __name__ == "__main__":
    main()