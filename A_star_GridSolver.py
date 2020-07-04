import random

start = None
end = None


class Node:
    # constructor
    def __init__(self, parent=None , position = None, next=None):
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


def findAllMoves(arr, coor,neighbourLL):
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
        node = Node(None,ncoor,None)
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

        if current.position == endNode.position:
            break

        neighbourLL = LinkedList()
        neighbours = findAllMoves(arr, current.position ,neighbourLL)
        while neighbours.pop():
            cost = current.g + 1
            if open.search(neighbour) is True:
                if getDistance(neighbour.coor, currentList) <= cost: continue
            elif closed.search(neighbour) is True:
                if getDistance(neighbour.coor, currentList) <= cost: continue
            else:
                open.newNode(neighbour)
                neighbour.h = getDistance(neighbour.coor, goalList)
            neighbour.g = cost


if __name__ == '__main__':
    listLL = LinkedList()

    node1 = Node()
    node1.f = 11
    listLL.push(node1)

    node2 = Node()
    node2.f = 20
    listLL.push(node2)

    node3 = Node()
    node3.f = 23
    listLL.push(node3)

    node4 = Node()
    node4.f = 25
    listLL.push(node4)

    node5 = Node()
    node5.f = 13
    listLL.push(node5)

    listLL.printLL()

    popped = listLL.pop()



    sizeOfGrid = 10
    arr = makeSquareGrid(sizeOfGrid)
    arr = fillGrid(arr)

    printGrid(arr)

    h = getDistance(start, end)

    startNode = Node(None,start,None)
    startNode.f = h
    endNode = Node(None,end,None)

    open = LinkedList()
    open.push(startNode)
    closed = LinkedList()

    solve(arr, open, closed)

    # printGrid(arr)
    printGrid(arr)
