import sys
import math

def main():
    sys.setrecursionlimit(100000)
    
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        coords = list(map(int, sys.stdin.readline().split()))
        x1, y1, x2, y2, x3, y3, x4, y4 = coords
        
        dist = lineSegmentDistance(x1, y1, x2, y2, x3, y3, x4, y4)
        print(f"{dist:.2f}")

def lineSegmentDistance(x1, y1, x2, y2, x3, y3, x4, y4):
    if segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
        return 0.0
    
    d1 = distance(x1, y1, x3, y3, x4, y4)
    d2 = distance(x2, y2, x3, y3, x4, y4)
    d3 = distance(x3, y3, x1, y1, x2, y2)
    d4 = distance(x4, y4, x1, y1, x2, y2)
    
    return min(d1, d2, d3, d4)

def segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    def cross(ax, ay, bx, by, cx, cy):
        return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    
    d1 = cross(x3, y3, x4, y4, x1, y1)
    d2 = cross(x3, y3, x4, y4, x2, y2)
    d3 = cross(x1, y1, x2, y2, x3, y3)
    d4 = cross(x1, y1, x2, y2, x4, y4)
    
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    
    if d1 == 0 and onSegment(x3, y3, x4, y4, x1, y1):
        return True
    if d2 == 0 and onSegment(x3, y3, x4, y4, x2, y2):
        return True
    if d3 == 0 and onSegment(x1, y1, x2, y2, x3, y3):
        return True
    if d4 == 0 and onSegment(x1, y1, x2, y2, x4, y4):
        return True
    
    return False

def onSegment(x1, y1, x2, y2, px, py):
    return (min(x1, x2) <= px <= max(x1, x2) and 
            min(y1, y2) <= py <= max(y1, y2))

def distance(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    if dx == 0 and dy == 0:
        return math.sqrt((px - x1) ** 2 + (py - y1) ** 2)
    
    t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
    t = max(0, min(1, t))
    
    closestX = x1 + t * dx
    closestY = y1 + t * dy
    
    return math.sqrt((px - closestX) ** 2 + (py - closestY) ** 2)

if __name__ == "__main__":
    main()