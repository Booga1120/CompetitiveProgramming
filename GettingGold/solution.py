import sys
import math

def main():
    sys.setrecursionlimit(10000)
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(m):
        row = sys.stdin.readline().strip()
        grid.append(list(row))
    
    gold = 0
    
    def floodFill(row, col):
        nonlocal gold
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        if grid[row][col] == '#' or grid[row][col] == '@':
            return
            
        if grid[row][col] == 'G':
            gold += 1

        grid[row][col] = '@'
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if 0 <= newRow < m and 0 <= newCol < n:  # Add bounds check here
                if grid[newRow][newCol] == 'T':
                    return
        
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            floodFill(newRow, newCol)

    
    for row in range(m):
        # print(grid[row])
        for col in range(n):
            if grid[row][col] == 'P':
                floodFill(row, col)
    
    print(gold)

if __name__ == "__main__":
    main()