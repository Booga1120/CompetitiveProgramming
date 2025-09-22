import sys
import math

def main():
    sys.setrecursionlimit(100000)
    input = int(sys.stdin.readline())
    coords = []
    for i in range(input):
        coords.append(list(map(int,sys.stdin.readline().strip().split())))# read in
    adjlist = dict()
    for coord in coords:
        coordFirst = tuple(coord[0:3])
        coordSecond = tuple(coord[3:6])
        
        if coordFirst not in adjlist:
            adjlist[coordFirst] = {coordSecond}
        else:
            adjlist[coordFirst].add(coordSecond)
        if coordSecond not in adjlist:
            adjlist[coordSecond] = {coordFirst}
        else:
            adjlist[coordSecond].add(coordFirst)
    
    if(traverse3d(adjlist)):
        print("True closed chains")
    else:
        print("No true closed chains")
    if(traverse2d(adjlist)):
        print("Floor closed chains")
    else:
        print("No floor closed chains")

    pass

def traverse3d(adjlist):
    visited = set()
    nodes = list(adjlist.keys())
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in adjlist[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for node in nodes:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

def traverse2d(adjlist):
    adjlist2d = {}
    
    for point, neighbors in adjlist.items():
        point2d = (point[0], point[1])
        if point2d not in adjlist2d:
            adjlist2d[point2d] = set()
        
        for neighbor in neighbors:
            neighbor2d = (neighbor[0], neighbor[1])
            if neighbor2d != point2d:
                adjlist2d[point2d].add(neighbor2d)
    
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        
        for neighbor in adjlist2d.get(node, set()):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        
        return False
    
    for node in adjlist2d:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

if __name__ == "__main__":
    main()