import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math

def main():
    sys.setrecursionlimit(100000)
    tests = int(sys.stdin.readline().strip())
    reachable = {1:{1,2,3,4,5,6,7,8,9,0}, 2:{2,3,5,6,8,9,0}, 3:{3,6,9}, 4:{4,5,6,7,8,9,0}, 
                 5:{5,6,8,9,0}, 6:{6,9}, 7:{7,8,9,0}, 8:{8,9,0}, 9:{9}, 0:{0}}
    
    def isValid(num):
        s = str(num)
        for i in range(len(s) - 1):
            if int(s[i+1]) not in reachable[int(s[i])]:
                return False
        return True
    
    def findClosest(target):
        if isValid(target):
            return target
        
        lower = target - 1
        upper = target + 1
        
        while lower >= 0 or upper <= 200:
            if lower >= 0 and isValid(lower):
                return lower
            if upper <= 200 and isValid(upper):
                return upper
            lower -= 1
            upper += 1
        
        return target
    
    for i in range(tests):
        inputNum = int(sys.stdin.readline().strip())
        result = findClosest(inputNum)
        print(result)

if __name__ == "__main__":
    main()