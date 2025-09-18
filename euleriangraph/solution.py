import sys
import math

def main():
    input = sys.stdin.readline().strip().split()
    verts = int(input[0])
    edges = int(input[1])
    
    in_degree = [0] * verts
    out_degree = [0] * verts
    
    # Read directed graph
    for i in range(edges):
        edge = list(map(int, sys.stdin.readline().strip().split()))
        start = edge[0]
        end = edge[1]
        out_degree[start-1] += 1
        in_degree[end-1] += 1
    
    # Iterate nodes, count incoming & outgoing edges, see if equal
    start = None
    end = None
    odd = 0
    
    for i in range(verts):
        outs = out_degree[i]
        ins = in_degree[i]
        
        if((ins+outs)%2==1):
            odd+=1
            if(ins>outs):
                end = i+1
            else:
                start = i+1
        elif(ins!=outs):
            print("no")
            return
            
    if(odd!=2 and odd != 0): # make sure odd degree vertices is exactly 2 or 0
        print("no")
        return
        
    if(start is not None and end is not None):
        print(str(start) + " " + str(end))
    else:
        print("anywhere")

if __name__ == "__main__":
    main()