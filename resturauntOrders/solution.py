import sys

def main():
    sys.setrecursionlimit(100000)
    
    n = int(sys.stdin.readline())
    costs = list(map(int, sys.stdin.readline().split()))
    
    maxSum = 30000
    ways = [0] * (maxSum + 1)
    parent = [-1] * (maxSum + 1)
    
    ways[0] = 1
    
    for i in range(n):
        c = costs[i]
        for s in range(c, maxSum + 1):
            if ways[s - c] > 0:
                if ways[s] == 0:
                    parent[s] = i
                elif ways[s] == 1 and parent[s] != i:
                    ways[s] = 2
                    continue
                
                if ways[s - c] == 1:
                    ways[s] = min(ways[s] + 1, 2)
                else:
                    ways[s] = 2
    
    m = int(sys.stdin.readline())
    orders = list(map(int, sys.stdin.readline().split()))
    
    for order in orders:
        if ways[order] == 0:
            print("Impossible")
        elif ways[order] >= 2:
            print("Ambiguous")
        else:
            result = []
            current = order
            while current > 0:
                itemIdx = parent[current]
                result.append(itemIdx + 1)
                current -= costs[itemIdx]
            result.sort()
            print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()