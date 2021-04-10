import sys
import reader
from location import Location

infi = sys.maxsize


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Node:
    def __init__(self, vertexNumber):
        self.vertexNumber = vertexNumber
        self.children = []

    def Add_child(self, vNumber, length):
        p = Pair(vNumber, length)
        self.children.append(p)


def dijkstraDist(g, s, path):

    dist = [infi for i in range(len(g))]

    visited = [False for i in range(len(g))]

    for i in range(len(g)):
        path[i] = -1
    dist[s] = 0
    path[s] = -1
    current = s

    sett = set()
    while (True):

        visited[current] = True
        for i in range(len(g[current].children)):
            v = g[current].children[i].first
            if (visited[v]):
                continue

            sett.add(v)
            alt = dist[current] + g[current].children[i].second

            if (alt < dist[v]):
                dist[v] = alt
                path[v] = current
        if current in sett:
            sett.remove(current)
        if (len(sett) == 0):
            break

        minDist = infi
        index = 0

        for a in sett:
            if (dist[a] < minDist):
                minDist = dist[a]
                index = a
        current = index
    return dist


def printPath(path, i, s):
    if (i != s):
        if (path[i] == -1):
            print(" Path not found!!")
            return
        printPath(path, path[i], s)
        print(" "+str(path[i]+1) + " ->",end="")


def distance(src, des):
    maxid = 0
    records = {}

    for record in reader.readloc("./locations.json"):
        if int(record["id"]) > maxid:
            maxid = int(record["id"])
        records[record["id"]] = Location.from_record(record)

    if(src+1 not in records.keys() or des+1 not in records.keys()):
        print(" Error: Enter location id doesn't exist ")
        return

    v = []
    for i in range(maxid):
        a = Node(i)
        v.append(a)

    for path in reader.readpaths("./paths.json"):
        v[path["start"]-1].Add_child(path["end"]-1,
                                     records[path["start"]].dist_to(records[path["end"]]))

    path = [0 for i in range(len(v))]
    dist = dijkstraDist(v, src, path)

    if (dist[des] == infi):
        print(" {} and {} are not connected".format(des+1, src+1))
    else:
        print(" Distance of {} location from source location {} is: {} km".format(
            des+1, src+1, dist[des]))
        printPath(path,des,src)
        print(" {}".format(des+1))
