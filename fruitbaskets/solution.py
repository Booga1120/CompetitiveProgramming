import sys
import math

def main():
    input = int(sys.stdin.readline())
    weights = list(map(int, sys.stdin.readline().split()))
    totalUnderWeight = fruitbasket(0, weights)

    #sum of all combinations of weights
    totalWeight = sum([weights[i] * (2 ** (input - 1)) for i in range(input)])
    print(totalWeight - totalUnderWeight)
    
    
    pass

def fruitbasket(currentWeight, weights):
    
    if len(weights) == 0:
        return currentWeight
    myweight = weights[0]
    if currentWeight+myweight >= 200:
        return fruitbasket(currentWeight, weights[1:])
    
    return fruitbasket(currentWeight + myweight, weights[1:]) + fruitbasket(currentWeight, weights[1:])

if __name__ == "__main__":
    main()