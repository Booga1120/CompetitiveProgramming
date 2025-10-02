import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000)
    n,k = map(int, sys.stdin.readline().split())

    lefthall = []
    righthall = []
    leftsum = 0
    rightsum = 0

    for i in range(k):
        a,b = map(int, sys.stdin.readline().split())
        lefthall.append(a)
        righthall.append(b)
        leftsum+=a
        rightsum+=b

    print(lefthall)
    print(righthall)
    print(leftsum)
    print(rightsum)
    
    if(leftsum > rightsum):
        solutions = [1]*k
    else:
        solutions = [3]*k

    def calc(path):
        sum = 0
        idx = 0
        for x in path:
            if x == 3:
                sum += righthall[idx]
            if x == 2:
                sum += righthall[idx]+lefthall[idx]
            if x == 1:
                sum += lefthall[idx]
            idx+=1
        return sum
    
    def swap(path,spot):
        idx = 0
        path[spot]=2
        for x in path:
            if idx > spot:
                path[idx]=4-idx
            idx+=1
    
    bonus = 0
    for i in range(n-k):
        a,b = map(int, sys.stdin.readline().split())
        lefthall.append(a)
        righthall.append(b)
        if(solutions[-1]==3):
            solutions.append(3)
        else:
            solutions.append(1)
        idx = 0
        bestPathValue = calc(solutions) #default to value if there was no swap
        didNotSwap = True
        for idx in range(len(solutions)):
            if(didNotSwap and solutions[idx] != 2):
                potentialSolution = swap(solutions, idx)
                potentialNewValue = calc(potentialSolution)
                if (potentialNewValue>=bestPathValue):
                    bestPathValue = potentialNewValue
                    solutions = potentialSolution
                    didNotSwap = False
                    print(idx)
        if(didNotSwap):
            bonus+=1

    unused = []
    result = 0
    for i in range(n):#find all unused grids, find current path value
        if(solutions[i]==1):
            unused.heappush(-righthall[i])
            result+=lefthall[i]
        elif(solutions[i]==3):
            unused.heappush(-lefthall[i])
            result+=righthall[i]
        else:
            result+=lefthall[i]+righthall[i]
    for i in range(bonus):
        result+=-heappop(unused)


    


if __name__ == "__main__":
    main()