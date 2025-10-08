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

def kmpSearch(pattern, text):
    m = len(pattern)
    n = len(text)
    
    if m > n:
        return []
    
    lps = computeLps(pattern)
    positions = []
    
    i = 0
    j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions

def main():
    sys.setrecursionlimit(100000)
    
    lines = []
    for line in sys.stdin:
        lines.append(line.rstrip('\n'))
    
    i = 0
    while i < len(lines):
        pattern = lines[i]
        if i + 1 < len(lines):
            text = lines[i + 1]
            positions = kmpSearch(pattern, text)
            if positions:
                print(' '.join(map(str, positions)))
            else:
                print()
        i += 2

if __name__ == "__main__":
    main()