import sys

def computeLps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def removeBugsKmp(line, bugMarker):
    if not bugMarker or not line:
        return line
    
    m = len(bugMarker)
    lps = computeLps(bugMarker)
    
    stack = []
    matchStack = []
    
    j = 0
    for char in line:
        stack.append(char)
        
        while j > 0 and char != bugMarker[j]:
            j = lps[j - 1]
        
        if char == bugMarker[j]:
            j += 1
        
        matchStack.append(j)
        
        if j == m:
            for _ in range(m):
                stack.pop()
                matchStack.pop()
            
            j = matchStack[-1] if matchStack else 0
    
    return ''.join(stack)

def main():
    sys.setrecursionlimit(100000)
    
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    
    i = 0
    firstTestCase = True
    
    while i < len(lines):
        parts = lines[i].split(' ', 1)
        numLines = int(parts[0])
        bugMarker = parts[1]
        
        if not firstTestCase:
            print()
        firstTestCase = False
        
        for j in range(i + 1, i + 1 + numLines):
            if j < len(lines):
                cleanedLine = removeBugsKmp(lines[j], bugMarker)
                print(cleanedLine)
        
        i += numLines + 1

if __name__ == "__main__":
    main()
