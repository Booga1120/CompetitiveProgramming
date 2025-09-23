import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    grid = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
    
    result = []
    for i in range(n):
        result.append([])
    
    def searchAir(row, col):
        if grid[row][col] == '.':
            return 0
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = [(row, col, 0)]
        visited = set([(row, col)])
                
        while queue:
            currentRow, currentCol, distance = queue.pop(0)
                        
            for dr, dc in directions:
                newRow = currentRow + dr
                newCol = currentCol + dc
                                
                if 0 <= newRow < n and 0 <= newCol < m:
                    if (newRow, newCol) not in visited:
                        if grid[newRow][newCol] == '.':
                            return distance + 1
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol, distance + 1))
                else:
                    return distance + 1
                
        return -1
        
    longestDistance = 0
        
    for a in range(n):
        for b in range(m):
            distance = searchAir(a, b)
            if distance > longestDistance:
                longestDistance = distance
            if grid[a][b] == '.':
                result[a].append('0')
            else:
                result[a].append(str(distance))
                
    numChars = 2 if longestDistance < 10 else 3
        
    for a in range(n):
        for b in range(m):
            if grid[a][b] == '.':
                result[a][b] = '.' * numChars
            else:
                result[a][b] = ('.' * (numChars - len(result[a][b]))) + result[a][b]
        
    for a in range(n):
        print(''.join(result[a]))

if __name__ == "__main__":
    main()