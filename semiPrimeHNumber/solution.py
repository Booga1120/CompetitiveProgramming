import sys
import math

def main():
    sys.setrecursionlimit(100000)
    
    maxVal = 1000002
    
    isHPrime = [False] * maxVal
    for i in range(5, maxVal, 4):
        isHPrime[i] = True
    
    hPrimes = []
    
    limit = int(math.sqrt(maxVal))
    
    for i in range(5, maxVal, 4):
        if i > limit:
            if isHPrime[i]:
                hPrimes.append(i)
            continue

        if isHPrime[i]:
            hPrimes.append(i)
            
            for j in range(i * i, maxVal, i * 4):
                isHPrime[j] = False

    isHSemiPrime = [False] * maxVal
    
    for i in range(len(hPrimes)):
        hPi = hPrimes[i]
        
        for j in range(i, len(hPrimes)):
            product = hPi * hPrimes[j]
            
            if product >= maxVal:
                break
            
            isHSemiPrime[product] = True
    
    arr = [0] * maxVal
    for i in range(1, maxVal):
        if isHSemiPrime[i]:
            arr[i] = 1
    
    treeSize = 4 * maxVal
    tree = [0] * treeSize
    
    def build(node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] + tree[2 * node + 1]
    
    def query(node, start, end, L, R):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return tree[node]
        mid = (start + end) // 2
        return query(2 * node, start, mid, L, R) + query(2 * node + 1, mid + 1, end, L, R)
    
    build(1, 0, maxVal - 1)
    
    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line:
                break
            h = int(line)
        except EOFError:
            break
        except ValueError:
            continue

        if h == 0:
            break
        
        query_h = min(h, maxVal - 1)
        
        count = query(1, 0, maxVal - 1, 1, query_h)
        
        print(f"{h} {count}")

if __name__ == "__main__":
    main()
