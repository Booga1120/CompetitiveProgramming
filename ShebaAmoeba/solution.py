import sys
from collections import defaultdict

def tarjanScc(graph, n):
    index = {}
    lowlink = {}
    onStack = {}
    idx = 0
    stack = []
    sccCount = 0
    
    def tarjan(v):
        nonlocal idx, sccCount
        index[v] = idx
        lowlink[v] = idx
        idx += 1
        stack.append(v)
        onStack[v] = True
        
        for w in graph[v]:
            if w not in index:
                tarjan(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onStack.get(w, False):
                lowlink[v] = min(lowlink[v], index[w])
        
        if lowlink[v] == index[v]:
            sccCount += 1
            while True:
                curr = stack.pop()
                onStack[curr] = False
                if curr == v:
                    break
    
    for vertex in range(1, n + 1):
        if vertex not in index:
            tarjan(vertex)
    
    return sccCount

def main():
    testCases = int(sys.stdin.readline().strip())
    
    for _ in range(testCases):
        n, m = map(int, sys.stdin.readline().split())
        
        graph = defaultdict(list)
        
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
        
        sccCount = tarjanScc(graph, n)
        print(sccCount)

if __name__ == "__main__":
    main()