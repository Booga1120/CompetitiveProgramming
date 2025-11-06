import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000)
    
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    maxLeft = [float('-inf')] * n
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i-1], arr[i-1])
    
    minRight = [float('inf')] * n
    for i in range(n-2, -1, -1):
        minRight[i] = min(minRight[i+1], arr[i+1])
    
    count = 0
    for i in range(n):
        if maxLeft[i] <= arr[i] and arr[i] < minRight[i]:
            count += 1
    
    print(count)

if __name__ == "__main__":
    main()