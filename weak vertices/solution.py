import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    gridsize = int(sys.stdin.readline())
    grid = []
    vertices = list(range(gridsize))

    for i in range(gridsize):
        grid.append(list(map(int,sys.stdin.readline().strip().split())))

    # print(gridsize)
    # print(grid)
    
    for i in range(gridsize):#semi bfs
        if(i not in vertices):
            continue
        visited = {i}
        for j in range(gridsize):
            if(i!=j and grid[i][j]==1):
                visited.add(j)
        for j in visited:
            for k in range(gridsize):
                if(grid[j][k]==1 and k != i and k in visited):
                    if(i in vertices):
                        vertices.remove(i)
                    if(j in vertices):
                        vertices.remove(j)
                    if(k in vertices):
                        vertices.remove(k)
    print(vertices)
                    

if __name__ == "__main__":
    main()