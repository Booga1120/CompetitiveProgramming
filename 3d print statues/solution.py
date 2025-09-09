import math
import sys

def main():
    input = int(sys.stdin.readline())

    print(math.ceil(math.log2(input))+1)

if __name__ == "__main__":
    main()
