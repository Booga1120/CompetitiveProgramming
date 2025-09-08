import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    input = sys.stdin.read
    data = input().splitlines()
    # Process the input data
    for line in data:
        numbers = list(map(int, line.split()))
        # Do something with the numbers
        print(sum(numbers))

    # Fast I/O (uncomment if needed for large inputs)
    # input = sys.stdin.readline
    
    # Common input patterns:
    
    # Single integer
    # n = int(input())
    
    # Multiple integers on one line
    # a, b = map(int, input().split())
    
    # List of integers
    # arr = list(map(int, input().split()))
    
    # Multiple lines of input
    # lines = []
    # for _ in range(n):
    #     lines.append(input().strip())
    
    # Read until EOF
    # lines = []
    # try:
    #     while True:
    #         lines.append(input().strip())
    # except EOFError:
    #     pass
    
    # YOUR CODE HERE
    
    pass

if __name__ == "__main__":
    main()