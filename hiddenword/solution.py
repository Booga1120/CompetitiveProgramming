import sys
import math

puzzle = [[]]

def main():
    puzzlesize = list(map(int, sys.stdin.readline().strip().split))
    
    for i in range(puzzlesize[0]):
        puzzle.append(list(sys.stdin.readline().strip().split()))

    numwords = int(sys.stdin.readline().strip())
    words = []
    for i in range(numwords):
        words.append(sys.stdin.readline().strip())
    
    for word in words:
        find(word)

    pass

class coordinate:
    row=0
    column=0

def find(word):
    coord = coordinate()
    for row in puzzle:
        for letter in row:
            if(letter == word[0]):
                search(coord, word[1:])
                return
        coord.column+=1
    coord.row+=1

def search(coord, word): #recursively search
    up = puzzle[coord.row][coord.column]
    

if __name__ == "__main__":
    main()