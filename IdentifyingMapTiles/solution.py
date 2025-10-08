import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline().strip()

    level=0
    xcoord = 0
    ycoord = 0
    while len(input)>0:
        # print(input)
        char = input[0]
        level += 1
        xcoord *=2
        ycoord *=2
        if(char == '1'):
            xcoord +=1
        elif(char == '2'):
            ycoord +=1    
        elif(char == '3'):
            xcoord+= 1
            ycoord += 1        

        input = input[1:]
    
    print(f"{level} {xcoord} {ycoord}")
    
    pass

if __name__ == "__main__":
    main()