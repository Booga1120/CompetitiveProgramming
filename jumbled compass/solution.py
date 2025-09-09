import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    b = int(sys.stdin.readline())
    a = int(sys.stdin.readline())
    
    if a < b:
        a += 360
    
    if a - 180 <= b:
        print(a-b)
    else:
        print(-b - (360 - a))
    
    pass

if __name__ == "__main__":
    main()