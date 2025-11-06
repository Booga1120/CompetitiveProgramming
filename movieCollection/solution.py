import sys

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
    
    def rangeQuery(self, left, right):
        if left > right:
            return 0
        return self.query(right) - (self.query(left - 1) if left > 0 else 0)

def main():
    sys.setrecursionlimit(100000)
    
    n = int(sys.stdin.readline())
    balls = []
    for i in range(n):
        pos = i
        order = int(sys.stdin.readline())
        balls.append((pos, order))
    
    orderToPos = {}
    for pos, order in balls:
        orderToPos[order] = pos
    
    ft = FenwickTree(n)
    for i in range(n):
        ft.update(i + 1, 1)
    
    totalMoves = 0
    currentPos = 0
    
    for dropOrder in range(1, n + 1):
        targetPos = orderToPos[dropOrder]
        
        if currentPos == targetPos:
            distance = 0
        else:
            clockwiseDist = 0
            pos = currentPos
            while True:
                pos = (pos + 1) % n
                if ft.query(pos + 1) - ft.query(pos) > 0:
                    clockwiseDist += 1
                if pos == targetPos:
                    break
            
            counterclockwiseDist = 0
            pos = currentPos
            while True:
                pos = (pos - 1 + n) % n
                if ft.query(pos + 1) - ft.query(pos) > 0:
                    counterclockwiseDist += 1
                if pos == targetPos:
                    break
            
            distance = min(clockwiseDist, counterclockwiseDist)
        
        totalMoves += distance + 1
        
        ft.update(targetPos + 1, -1)
        
        if dropOrder < n:
            pos = targetPos
            while True:
                pos = (pos + 1) % n
                if ft.query(pos + 1) - ft.query(pos) > 0:
                    currentPos = pos
                    break
    
    print(totalMoves)

if __name__ == "__main__":
    main()