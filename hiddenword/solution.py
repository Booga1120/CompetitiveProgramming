import sys
from collections import defaultdict

def main():
    puzzlesize = list(map(int, sys.stdin.readline().strip().split()))
    rows, cols = puzzlesize[0], puzzlesize[1]
    
    puzzle = []
    for i in range(rows):
        puzzle.append(sys.stdin.readline().strip())
    
    numwords = int(sys.stdin.readline().strip())
    words = []
    for i in range(numwords):
        words.append(sys.stdin.readline().strip())
    
    letter_positions = defaultdict(list)
    for row in range(rows):
        for col in range(cols):
            letter_positions[puzzle[row][col]].append((row, col))
    
    words_by_first_letter = defaultdict(list)
    for word in words:
        if word and word[0] in letter_positions:
            words_by_first_letter[word[0]].append(word)
    
    count = 0
    visited = [[False] * cols for _ in range(rows)]
    
    for first_letter, word_group in words_by_first_letter.items():
        positions = letter_positions[first_letter]
        for word in word_group:
            found = False
            for row, col in positions:
                if dfs(puzzle, word, 1, row, col, visited, rows, cols):
                    found = True
                    break
            if found:
                count += 1
    
    print(count)

def dfs(puzzle, word, pos, row, col, visited, rows, cols):
    if pos == len(word):
        return True
    
    visited[row][col] = True
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc
        
        if (0 <= new_row < rows and 0 <= new_col < cols and
            not visited[new_row][new_col] and
            puzzle[new_row][new_col] == word[pos]):
            
            if dfs(puzzle, word, pos + 1, new_row, new_col, visited, rows, cols):
                visited[row][col] = False
                return True
    
    visited[row][col] = False
    return False

if __name__ == "__main__":
    main()