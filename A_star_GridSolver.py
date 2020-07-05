import random

start = None
end = None


class Node:
    # constructor
    def __init__(self, parent=None, position=None, next=None):
        self.parent = parent
        self.position = position
        self.f = 0
        self.h = 0
        self.g = 0
        self.next = next

    def __eq__(self, other):
        return self.position == other.position

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_node):

        if self.head is None:
            self.head = new_node
            return

        ptr = self.head
        prev = None

        while ptr is not None:
            if ptr.f >= new_node.f:

                if prev is None:
                    new_node.next = ptr
                    self.head = new_node
                    return
                else:
                    prev.next = new_node
                    new_node.next = ptr
                    return
            prev = ptr
            ptr = ptr.next
        prev.next = new_node
        return

    def pop(self):
        ptr = self.head
        if self.head is None:
            return False
        else:
            self.head = ptr.next
            ptr.next = None
            return ptr

    def find(self, check_node):
        ptr = self.head
        while ptr is not None:
            if ptr.position == check_node.position:
                return ptr
            else:
                ptr = ptr.next
        return None

    def printLL(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.f)
            ptr = ptr.next


def makeSquareGrid(row):
    arr = [[None] * row for _ in range(row)]
    return arr


def fillGrid(arr):
    row = len(arr)
    size = row * row
    for x in range(0, int(size * 30 / 100)):
        i = random.randint(0, row - 1)
        j = random.randint(0, row - 1)
        arr[i][j] = -1

    check = True
    while check:
        i = random.randint(0, row - 1)
        j = random.randint(0, row - 1)
        if arr[i][j] is None:
            arr[i][j] = 'A'
            global start
            start = (i, j)
            check = False
    check = True
    while check:
        i = random.randint(0, row - 1)
        j = random.randint(0, row - 1)
        if arr[i][j] is None:
            arr[i][j] = 'T'
            global end
            end = (i, j)
            check = False

    return arr


def printGrid(arr):
    s = [[str(e) for e in row] for row in arr]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    global start
    global end
    print(start, end)


def getDistance(startCoor, endCoor):
    distance = abs(startCoor[0] - endCoor[0]) + abs(startCoor[1] - endCoor[1])
    return distance


def getNorth(coor):
    tempc = [coor[0] - 1, coor[1]]
    return tempc


def getSouth(coor):
    tempc = [coor[0] + 1, coor[1]]
    return tempc


def getEast(coor):
    tempc = [coor[0], coor[1] + 1]
    return tempc


def getWest(coor):
    tempc = [coor[0], coor[1] - 1]
    return tempc


def findAllMoves(arr, coor, neighbourLL):
    global end
    n = None
    s = None
    e = None
    w = None
    ncoor = None
    scoor = None
    ecoor = None
    wcoor = None

    coorList = list(coor)
    neighbours = []

    if 0 <= getNorth(coorList)[0] < len(arr) and (
            arr[getNorth(coorList)[0]][coorList[1]] is None or arr[getNorth(coorList)[0]][coorList[1]] == 'T'):
        ncoor = getNorth(coorList)
        node = Node(None, ncoor, None)
        neighbourLL.push(node)

    if 0 <= getSouth(coorList)[0] < len(arr) and (
            arr[getSouth(coorList)[0]][coorList[1]] is None or arr[getSouth(coorList)[0]][coorList[1]] == 'T'):
        scoor = getSouth(coorList)
        node = Node(None, scoor, None)
        neighbourLL.push(node)
    if 0 <= getEast(coorList)[1] < len(arr) and (
            arr[coorList[0]][getEast(coorList)[1]] is None or arr[coorList[0]][getEast(coorList)[1]] == 'T'):
        ecoor = getEast(coorList)
        node = Node(None, ecoor, None)
        neighbourLL.push(node)
    if 0 <= getWest(coorList)[1] < len(arr) and (
            arr[coorList[0]][getWest(coorList)[1]] is None or arr[coorList[0]][getWest(coorList)[1]] == 'T'):
        wcoor = getWest(coorList)
        node = Node(None, wcoor, None)
        neighbourLL.push(node)

    return neighbourLL


def solve(arr, open, closed):
    while open.head is not None:

        current = open.pop()

        if current.position == list(endNode.position):
            break

        neighbourLL = LinkedList()
        neighbours = findAllMoves(arr, current.position, neighbourLL)
        while neighbours.head is not None:
            neighbour = neighbours.pop()
            cost = current.g + 1
            nodeOpen = open.find(neighbour)
            nodeClosed = closed.find(neighbour)
            if nodeOpen is not None:
                if nodeOpen.g <= cost: continue
            elif nodeClosed is not None:
                if nodeClosed.g <= cost: continue
                prev = closed.head
                if prev == nodeClosed:
                    closed.pop()
                    nodeClosed.g = cost
                    nodeClosed.parent = current
                    nodeClosed.f = nodeClosed.g + nodeClosed.h
                    open.push(nodeClosed)
                    continue
                while prev.next != nodeClosed:
                    prev = prev.next
                prev.next = nodeClosed.next
                nodeClosed.next = None
                nodeClosed.g = cost
                nodeClosed.parent = current
                nodeClosed.f = nodeClosed.g + nodeClosed.h
                open.push(nodeClosed)
                continue
            else:
                neighbour.h = getDistance(neighbour.position, end)
                neighbour.g = cost
                neighbour.f = neighbour.h + neighbour.g
                neighbour.parent = current
                open.push(neighbour)
        closed.push(current)
    if current.position == list(endNode.position):
        current = current.parent
        while current is not None:
            nodepos = current.position
            if arr[nodepos[0]][nodepos[1]] != 'A':
                arr[current.position[0]][current.position[1]] = "////"
            current = current.parent
    else:
        print("NO SOLUTION")


def removeNone(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] is None:
                arr[i][j] = -1


if __name__ == '__main__':

    sizeOfGrid = 101
    arr = makeSquareGrid(sizeOfGrid)
    arr = fillGrid(arr)

    printGrid(arr)

    h = getDistance(start, end)

    startNode = Node(None, start, None)
    startNode.f = h
    endNode = Node(None, end, None)

    open = LinkedList()
    open.push(startNode)
    closed = LinkedList()

    solve(arr, open, closed)

    # printGrid(arr)

    removeNone(arr)
    printGrid(arr)

