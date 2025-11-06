import sys

def crossProduct(ax, ay, bx, by, cx, cy):
    abx = bx - ax
    aby = by - ay
    acx = cx - ax
    acy = cy - ay
    return abx * acy - aby * acx

def onSegment(pix, piy, pjx, pjy, pkx, pky):
    return (min(pix, pjx) <= pkx <= max(pix, pjx) and
            min(piy, pjy) <= pky <= max(piy, pjy))

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = crossProduct(x3, y3, x4, y4, x1, y1)
    d2 = crossProduct(x3, y3, x4, y4, x2, y2)
    d3 = crossProduct(x1, y1, x2, y2, x3, y3)
    d4 = crossProduct(x1, y1, x2, y2, x4, y4)
    
    eps = 1e-9
    
    if ((d1 > eps and d2 < -eps) or (d1 < -eps and d2 > eps)) and \
       ((d3 > eps and d4 < -eps) or (d3 < -eps and d4 > eps)):
        return True
    
    if abs(d1) < eps and onSegment(x3, y3, x4, y4, x1, y1):
        return True
    if abs(d2) < eps and onSegment(x3, y3, x4, y4, x2, y2):
        return True
    if abs(d3) < eps and onSegment(x1, y1, x2, y2, x3, y3):
        return True
    if abs(d4) < eps and onSegment(x1, y1, x2, y2, x4, y4):
        return True
    
    return False

def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
    eps = 1e-9
    
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3
    
    cross = dx1 * dy2 - dy1 * dx2
    
    if abs(cross) < eps:
        d1 = crossProduct(x1, y1, x2, y2, x3, y3)
        d2 = crossProduct(x1, y1, x2, y2, x4, y4)
        
        if abs(d1) < eps and abs(d2) < eps:
            points = []
            if onSegment(x1, y1, x2, y2, x3, y3):
                points.append((x3, y3))
            if onSegment(x1, y1, x2, y2, x4, y4):
                points.append((x4, y4))
            if onSegment(x3, y3, x4, y4, x1, y1):
                points.append((x1, y1))
            if onSegment(x3, y3, x4, y4, x2, y2):
                points.append((x2, y2))
            
            uniquePoints = []
            for p in points:
                isUnique = True
                for up in uniquePoints:
                    if abs(p[0] - up[0]) < eps and abs(p[1] - up[1]) < eps:
                        isUnique = False
                        break
                if isUnique:
                    uniquePoints.append(p)
            
            if len(uniquePoints) == 0:
                return None
            elif len(uniquePoints) == 1:
                return uniquePoints[0]
            else:
                uniquePoints.sort()
                return (uniquePoints[0], uniquePoints[1])
        else:
            return None
    else:
        t = ((x3 - x1) * dy2 - (y3 - y1) * dx2) / cross
        
        if -eps <= t <= 1 + eps:
            ix = x1 + t * dx1
            iy = y1 + t * dy1
            return (ix, iy)
        else:
            return None

def main():
    n = int(sys.stdin.readline())
    
    for _ in range(n):
        coords = list(map(int, sys.stdin.readline().split()))
        x1, y1, x2, y2, x3, y3, x4, y4 = coords
        
        if not isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
            print("none")
        else:
            result = findIntersection(x1, y1, x2, y2, x3, y3, x4, y4)
            
            if result is None:
                print("none")
            elif isinstance(result, tuple) and len(result) == 2 and isinstance(result[0], tuple):
                p1, p2 = result
                print(f"{p1[0]:.2f} {p1[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}")
            else:
                print(f"{result[0]:.2f} {result[1]:.2f}")

if __name__ == "__main__":
    main()