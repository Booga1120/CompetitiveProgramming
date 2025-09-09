import sys
import datetime

def main():
    testcases = int(sys.stdin.read())

    for i in testcases:
        bookingcleaningtime = sys.stdin.readline().split()
        #store room details using array of pairs
        rooms = [[]]
        for j in bookingcleaningtime[0]:
            bookingdetail = sys.stdin.readline().split()
            arrivalTime = datetime.strptime(bookingcleaningtime[1]+"-"+bookingcleaningtime[2], "%Y-%m-%d-%H:%M")
            departureTime = datetime.strptime(bookingcleaningtime[3]+"-"+bookingcleaningtime[4], "%Y-%m-%d-%H:%M")
            rooms.append([arrivalTime, departureTime])

        # Do something with the numbers
        print(sum(numbers))

    # Fast I/O (uncomment if needed for large inputs)
    # input = sys.stdin.readline
    
    # Common input patterns:
    
    # Single integer
    # n = int(input())
    
    # Multiple integers on one line
    # a, b = map(int, input().split())
    
    # List of integers
    # arr = list(map(int, input().split()))
    
    # Multiple lines of input
    # lines = []
    # for _ in range(n):
    #     lines.append(input().strip())
    
    # Read until EOF
    # lines = []
    # try:
    #     while True:
    #         lines.append(input().strip())
    # except EOFError:
    #     pass
    
    # YOUR CODE HERE
    
    pass

if __name__ == "__main__":
    main()