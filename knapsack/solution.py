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
            weights.append(list(map(int, sys.stdin.readline().split())))
        
        dp = [[0] * (capacity + 1) for _ in range(numw + 1)]
        
        for i in range(numw):
            value, weight = weights[i][0], weights[i][1]
            for w in range(capacity + 1):
                dp[i + 1][w] = dp[i][w]
                if weight <= w:
                    dp[i + 1][w] = max(dp[i + 1][w], dp[i][w - weight] + value)
        
        selected = []
        w = capacity
        for i in range(numw - 1, -1, -1):
            if dp[i + 1][w] != dp[i][w]:
                selected.append(i)
                weight = weights[i][1]
                w -= weight
        
        selected.reverse()
        
        print(len(selected))
        if selected:
            print(' '.join(map(str, selected)))
        else:
            print()

if __name__ == "__main__":
    main()