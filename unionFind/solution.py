import sys

def main():
    sys.setrecursionlimit(100000)
    
    n, q = map(int, sys.stdin.readline().split())
    
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            nextNode = parent[x]
            parent[x] = root
            x = nextNode
        return root
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        
        if rootX == rootY:
            return
        
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootX] = rootY
            rank[rootY] += 1
    
    for _ in range(q):
        line = sys.stdin.readline().split()
        operation = line[0]
        a = int(line[1])
        b = int(line[2])
        
        if operation == '=':
            union(a, b)
        else:
            if find(a) == find(b):
                print("yes")
            else:
                print("no")

if __name__ == "__main__":
    main()