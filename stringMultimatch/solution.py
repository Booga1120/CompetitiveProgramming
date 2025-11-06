import sys
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.patternIdx = -1
        self.fail = None
    
    def insert(self, s, idx, patternIdx):
        if idx < len(s):
            if s[idx] not in self.children:
                self.children[s[idx]] = TrieNode()
            self.children[s[idx]].insert(s, idx + 1, patternIdx)
        else:
            self.end = True
            self.patternIdx = patternIdx

def buildFailureLinks(root):
    queue = deque()
    root.fail = root
    
    for child in root.children.values():
        child.fail = root
        queue.append(child)
    
    while queue:
        current = queue.popleft()
        
        for char, child in current.children.items():
            queue.append(child)
            
            failNode = current.fail
            while failNode != root and char not in failNode.children:
                failNode = failNode.fail
            
            if char in failNode.children and failNode.children[char] != child:
                child.fail = failNode.children[char]
            else:
                child.fail = root

def main():
    sys.setrecursionlimit(100000)
    
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        
        n = int(line.strip())
        patterns = []
        for _ in range(n):
            patterns.append(sys.stdin.readline().strip())
        
        text = sys.stdin.readline().strip()
        
        root = TrieNode()
        for i, pattern in enumerate(patterns):
            root.insert(pattern, 0, i)
        
        buildFailureLinks(root)
        
        results = [[] for _ in range(n)]
        node = root
        
        for pos in range(len(text)):
            char = text[pos]
            
            while node != root and char not in node.children:
                node = node.fail
            
            if char in node.children:
                node = node.children[char]
            
            tempNode = node
            while tempNode != root:
                if tempNode.end:
                    startPos = pos - len(patterns[tempNode.patternIdx]) + 1
                    results[tempNode.patternIdx].append(startPos)
                tempNode = tempNode.fail
        
        for positions in results:
            print(' '.join(map(str, positions)))

if __name__ == "__main__":
    main()