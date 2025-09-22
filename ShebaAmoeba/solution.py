import sys
import math

def main():
    m, n = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(m):
        grid.append(sys.stdin.readline().strip())
    
    visited = [[False] * n for _ in range(m)]
    whiteRegions = 0
    
    def floodFill(row, col):
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        if visited[row][col] or grid[row][col] == '#':
            return
        
        visited[row][col] = True
        
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for dr, dc in directions:
            floodFill(row + dr, col + dc)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.' and not visited[i][j]:
                floodFill(i, j)
                whiteRegions += 1
    
    print(whiteRegions - 1)

if __name__ == "__main__":
    main()