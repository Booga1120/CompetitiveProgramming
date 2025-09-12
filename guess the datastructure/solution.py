import sys
from heapq import heappush, heappop

def main():
    for line in sys.stdin:
        operations = int(line.strip())
        
        stack = []
        queue = []
        pqueue = []
        
        isStack = True
        isQueue = True
        isPQueue = True
        
        for i in range(operations):
            operation = sys.stdin.readline().split()
            type = int(operation[0])
            value = int(operation[1])
            
            if type == 1:
                stack.append(value)
                queue.append(value)
                heappush(pqueue, -value)
                
            elif type == 2:
                if ((not stack) or (stack.pop() != value)):
                    isStack = False
                if ((not queue) or (queue.pop(0) != value)):
                    isQueue = False
                if ((not pqueue) or (-heappop(pqueue) != value)):
                    isPQueue = False
        
        count = sum([isStack, isQueue, isPQueue])
        
        if count == 0:
            print("impossible")
        elif count > 1:
            print("not sure")
        elif isStack:
            print("stack")
        elif isQueue:
            print("queue")
        else:  # isPQueue
            print("priority queue")

if __name__ == "__main__":
    main()