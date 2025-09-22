import sys
import math

def main():
    m, n = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(m):
        row = sys.stdin.readline().strip()
        grid.append(list(row))
    
    whiteRegions = 0
    
    def floodFill(row, col):
        if grid[row][col] == '#':
            grid[row][col] = '.'
            directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    if grid[newRow][newCol] == '#':
                        floodFill(newRow, newCol)

    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                floodFill(row, col)
                whiteRegions += 1
    
    print(whiteRegions)

if __name__ == "__main__":
    main()