import sys

def main():
    sys.setrecursionlimit(100000)
    
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        
        polygon = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            polygon.append((x, y))
        
        m = int(sys.stdin.readline())
        for _ in range(m):
            px, py = map(int, sys.stdin.readline().split())
            result = pointInPolygon(polygon, (px, py))
            print(result)

def pointInPolygon(polygon, point):
    n = len(polygon)
    px, py = point
    
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        if pointOnSegment(p1, p2, point):
            return "on"
    
    crossings = 0
    for i in range(n):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % n]
        
        if rayCrossesSegment(p1, p2, point):
            crossings += 1
    
    if crossings % 2 == 1:
        return "in"
    else:
        return "out"

def pointOnSegment(p1, p2, point):
    x1, y1 = p1
    x2, y2 = p2
    px, py = point
    
    crossProduct = (py - y1) * (x2 - x1) - (px - x1) * (y2 - y1)
    if crossProduct != 0:
        return False
    
    if px < min(x1, x2) or px > max(x1, x2):
        return False
    if py < min(y1, y2) or py > max(y1, y2):
        return False
    
    return True

def rayCrossesSegment(p1, p2, point):
    x1, y1 = p1
    x2, y2 = p2
    px, py = point
    
    if y1 == y2:
        return False
    
    if py < min(y1, y2) or py >= max(y1, y2):
        return False
    
    if px >= max(x1, x2):
        return False
    
    if px < min(x1, x2):
        return True
    
    xIntersection = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
    
    if px < xIntersection:
        return True
    
    return False

if __name__ == "__main__":
    main()