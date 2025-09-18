import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    while True:
        line = sys.stdin.readline()
        if not line:  # EOF reached
            break
        gridsize = int(line.strip())
        grid = []
        vertices = list(range(gridsize))

        for i in range(gridsize):
            grid.append(list(map(int,sys.stdin.readline().strip().split())))

        # print(gridsize)
        # print(grid)
        
        for i in range(gridsize):#semi bfs
            # print(f"checking {i}:")
            if(i not in vertices):
                continue
            visited = {i}
            # print(f"corresponding neighbors: {grid[i]}")
            for j in range(gridsize):
                if(i!=j and grid[i][j]==1):
                    visited.add(j)
                    # print(f"added {j}")
            for j in visited:
                if(j == i):
                    continue
                # print(f"checking {j} for last piece of triangle")
                for k in range(gridsize):
                    if(grid[j][k]==1 and k != i and k in visited and j!=k):
                        # print(f"found triangle: {i}, {j}, {k}")
                        if(i in vertices):
                            vertices.remove(i)
                        if(j in vertices):
                            vertices.remove(j)
                        if(k in vertices):
                            vertices.remove(k)
        print(*vertices)
                    

if __name__ == "__main__":
    main()