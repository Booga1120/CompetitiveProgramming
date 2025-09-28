import sys
from collections import defaultdict

def tarjanScc(graph):
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
            newScc = []
            while True:
                curr = stack.pop()
                onStack[curr] = False
                newScc.append(curr)
                if curr == v:
                    break
            sccs.append(newScc)
    
    for vertex in graph:
        if vertex not in index:
            tarjan(vertex)
    
    return sccs

n = int(sys.stdin.readline().strip())
graph = defaultdict(list)
people = set()

for _ in range(n):
    line = sys.stdin.readline().strip().split()
    person = line[0]
    speaks = line[1]
    understands = line[2:] if len(line) > 2 else []
    
    people.add(person)
    
    graph[person].append(speaks)
    graph[speaks].append(person)
    
    for lang in understands:
        graph[lang].append(person)

sccs = tarjanScc(graph)

maxPeopleInScc = 0
for scc in sccs:
    peopleCount = sum(1 for node in scc if node in people)
    maxPeopleInScc = max(maxPeopleInScc, peopleCount)

result = n - maxPeopleInScc
print(result)