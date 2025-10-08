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
    n = len(line)
    lps = computeLps(bugMarker)
    
    result = []
    j = 0
    
    for i in range(n):
        result.append(line[i])
        j += 1
        
        while j >= m and result[-m:] == list(bugMarker):
            for _ in range(m):
                result.pop()
            j = len(result)
            
            matchLen = 0
            for k in range(min(j, m - 1), 0, -1):
                if result[-k:] == list(bugMarker[:k]):
                    matchLen = k
                    break
            j = matchLen
    
    return ''.join(result)

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