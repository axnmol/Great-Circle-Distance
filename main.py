import reader
import graph
from location import Location

LOC_FILE = "./locations.json"
PATH_FILE = "./paths.json"

def gcdistance():
    print("\n Enter coordinates of two locations to find great circle distance between them\n")
    lat1 = input(" Enter latitude of first location: ")
    lon1 = input(" Enter longitude of first location: ")
    lat2 = input(" Enter latitude of second location: ")
    lon2 = input(" Enter longitude of second location: ")

    location1 = Location(float(lat1), float(lon1))
    location2 = Location(float(lat2), float(lon2))

    print(" The Great Circle Distance between the given locations is: {} km".format(
        location1.dist_to(location2)))


def withinR():
    try:
        r = float(input("\n Enter the covering radius R(km): "))
    except ValueError:
        raise ValueError("That's not a Float!")
    print("\n Enter coordinates of location to find locations wihtin {} km".format(r))
    lat = input(" Enter latitude of location: ")
    lon = input(" Enter longitude of location: ")
    print()

    loc = Location(float(lat), float(lon))

    for record in reader.readloc(LOC_FILE):
        mockloc = Location.from_record(record)
        if mockloc.within_dist(loc, r):
            print(" Id: {}\tLatitude: {}\tLongitude: {}\tDistance: {} km".format(
                record["id"], record["latitude"], record["longitude"], mockloc.dist_to(loc)))

def shortestpath():
    try:
        src = int(input("\n Enter source location id: "))
        des = int(input(" Enter destination location id: "))
    except ValueError:
        raise ValueError("That's not a Int!")
    
    graph.distance(src-1,des-1)

if __name__ == "__main__":

    while True:
        print("\n----------------------------------------------------------")
        print(" 1. Calculate Great Circle Distance between two positions")
        print(" 2. Print locations within R kilometers radius")
        print(" 3. Print shortest path from source to destination")
        print(" 4. Exit\n")

        try:
            x = int(input(" Enter your choice: "))
        except ValueError:
            raise ValueError("That's not an int!")

        if x == 1:
            gcdistance()

        elif x == 2:
            withinR()

        elif x == 3:
            shortestpath()

        else:
            break
