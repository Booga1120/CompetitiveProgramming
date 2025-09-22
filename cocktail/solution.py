import sys
from heapq import heappush, heappop

def main():
   
    input = list(map(int,sys.stdin.readline().split()))
    result = True
    time = 0

    for i in range(input[0]):
        potion = int(sys.stdin.readline())
        if (time >= potion):
            result = False
        time += input[1]
    

    if(result):
        print("YES")
    else:
        print("NO")


    
    # Multiple integers on one line
    # a, b = map(int, input().split())
    
    # Read until EOF
    # for line in sys.stdin:
    
    # YOUR CODE HERE
    
    pass

if __name__ == "__main__":
    main()