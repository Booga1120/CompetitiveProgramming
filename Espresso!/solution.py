import sys

def main():
    input = sys.stdin.readline().split()
    n = int(input[0])
    s = int(input[1])
    maximum = s
    refill = 0
    for student in range(n):
        order = sys.stdin.readline()
        water = int(order[0])
        if(order.__contains__("L")):
            water += 1
        if(s< water):
            s = maximum
            refill += 1
        s -= water

    print(refill)
    
    pass

if __name__ == "__main__":
    main()