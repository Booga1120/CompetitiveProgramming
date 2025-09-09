import sys
import datetime

class Booking:
    content = ""
    arrivalTime = None
    departureTime = None
    endTime = None


def main():
    testcases = int(sys.stdin.readline())
    # print(testcases)

    for i in range(testcases):
        bookingcleaningtime = sys.stdin.readline().split()
        #store room details using array of pairs
        rooms = []
        for j in range(int(bookingcleaningtime[0])):
            bookingdetail = Booking()
            bookingdetail.content = sys.stdin.readline().split()
            # print(bookingdetail.content)
            bookingdetail.arrivalTime = datetime.datetime.strptime(bookingdetail.content[1]+"-"+bookingdetail.content[2], "%Y-%m-%d-%H:%M")
            bookingdetail.departureTime = datetime.datetime.strptime(bookingdetail.content[3]+"-"+bookingdetail.content[4], "%Y-%m-%d-%H:%M")
            bookingdetail.endTime = bookingdetail.departureTime + datetime.timedelta(minutes=int(bookingcleaningtime[1]))
            rooms.append(bookingdetail)
        
        #greedy approach
        rooms.sort(key=lambda x: x.arrivalTime)
        finalrooms = []
        # print(rooms)

        for room in rooms:
            if (finalrooms.__len__() == 0):# First room
                finalrooms.append(room)
                continue
            roomfound = False
            for totaldetail in finalrooms:
                if (room.arrivalTime >= totaldetail.endTime):# Can use existing room
                    totaldetail.endTime = room.endTime
                    roomfound = True
                    break
            if not roomfound:
                finalrooms.append(room)
        # print(finalrooms)
        print(len(finalrooms))
    pass

if __name__ == "__main__":
    main()