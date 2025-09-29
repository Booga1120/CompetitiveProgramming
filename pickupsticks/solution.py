import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    graph = [[] for x in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    
    while queue:
        stick = queue.popleft()
        result.append(stick)
        
        for bottom in graph[stick]:
            indegree[bottom] -= 1
            if indegree[bottom] == 0:
                queue.append(bottom)
    
    if len(result) == n:
        for stick in result:
            print(stick)
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()