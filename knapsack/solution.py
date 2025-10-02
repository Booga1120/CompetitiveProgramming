import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000)
    while True:
        line = sys.stdin.readline().split()
        if not line: break
        capacity, numw = int(line[0]), int(line[1])
        weights = []
        for i in range(numw):
            weights.append(list(map(int,sys.stdin.readline().split())))
        
        dp = [[]]*capacity
        for i in range(capacity):
            localSolution = []#this should be the optimal solution for dp[i]
            bestValue = 0
            for w in weights:
                value = w[0]
                weight = w[1]
                #if i still have capacity
                a = i-weight
                
                if(weight+(sum(x[1] for x in dp[i-weight]) if i-weight>=0 else 0)<=i+1):
                    localValue = value+(sum(x for x in dp[i-weight][0]) if i-weight>0 else 0)
                    if(localValue>bestValue):
                        localSolution.extend((dp[i-weight]) if i-weight>=0 else [])
                        localSolution.append(w)
                        bestValue = localValue
                        dp[i] = localSolution
        #I should now have ideal local solutions for each index
        print(dp[-1])
                


                    
                

    
    pass

if __name__ == "__main__":
    main()