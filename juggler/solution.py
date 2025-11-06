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

def main():
    sys.setrecursionlimit(100000)
    
    n = int(sys.stdin.readline())
    balls = []
    for i in range(n):
        order = int(sys.stdin.readline())
        balls.append(order)
    
    orderToPos = [0] * (n + 1)
    for pos in range(n):
        orderToPos[balls[pos]] = pos
    
    ft = FenwickTree(n)
    for i in range(n):
        ft.update(i + 1, 1)
    
    totalMoves = 0
    currentIdx = 0
    
    for dropOrder in range(1, n + 1):
        targetPos = orderToPos[dropOrder]
        targetIdx = ft.query(targetPos + 1)
        
        remaining = ft.query(n)
        clockwiseDist = (targetIdx - currentIdx - 1 + remaining) % remaining
        
        totalMoves += clockwiseDist + 1
        
        ft.update(targetPos + 1, -1)
        currentIdx = targetIdx - 1
    
    print(totalMoves)

if __name__ == "__main__":
    main()