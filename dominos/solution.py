import sys
from collections import defaultdict


def main():
    sys.setrecursionlimit(100000)
    testCases = int(sys.stdin.readline().strip())
    
    for _ in range(testCases):
        n, m = map(int, sys.stdin.readline().split())
        
        graph = defaultdict(list)
        
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
        
        sccs = tarjanScc(graph, n)
        
        nodeToScc = {}
        for i, scc in enumerate(sccs):
            for node in scc:
                nodeToScc[node] = i
        
        sccIndegree = [0] * len(sccs)
        
        for node in range(1, n + 1):
            for neighbor in graph[node]:
                if nodeToScc[node] != nodeToScc[neighbor]:
                    sccIndegree[nodeToScc[neighbor]] += 1
        
        result = sum(1 for indegree in sccIndegree if indegree == 0)
        print(result)


def tarjanScc(graph, n):
    index = {}
    lowlink = {}
    onStack = {}
    idx = 0
    stack = []
    sccs = []
    
    def tarjan(v):
        nonlocal idx
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
            scc = []
            while True:
                curr = stack.pop()
                onStack[curr] = False
                scc.append(curr)
                if curr == v:
                    break
            sccs.append(scc)
    
    for vertex in range(1, n + 1):
        if vertex not in index:
            tarjan(vertex)
    
    return sccs

if __name__ == "__main__":
    main()