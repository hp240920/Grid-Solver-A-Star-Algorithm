import random
import copy

start = None
end = None


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


class Directions:
    def __init__(self, north, south, east, west):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def __init__(self, direction):
        self.north = direction[0]
        self.south = direction[1]
        self.east = direction[2]
        self.west = direction[3]


def getDistance(startCoor, endCoor):
    distance = abs(startCoor[0] - endCoor[0]) + abs(startCoor[1] - endCoor[1])
    return distance


def getNorth(coor):
    tempc = [coor[0] - 1, coor[1]];
    return tempc


def getSouth(coor):
    tempc = [coor[0] + 1, coor[1]];
    return tempc;


def getEast(coor):
    tempc = [coor[0], coor[1] + 1];
    return tempc


def getWest(coor):
    tempc = [coor[0], coor[1] - 1];
    return tempc


def findBestMove(arr, coor):
    global end
    n = 1000
    s = 1000
    e = 1000
    w = 1000
    coorList = list(coor)

    if 0 <= getNorth(coorList)[0] < len(arr) and (
            arr[getNorth(coorList)[0]][coorList[1]] is None or arr[getNorth(coorList)[0]][coorList[1]] == 'T'):
        n = getDistance(getNorth(coorList), end)
    if 0 <= getSouth(coorList)[0] < len(arr) and (
            arr[getSouth(coorList)[0]][coorList[1]] is None or arr[getSouth(coorList)[0]][coorList[1]] == 'T'):
        s = getDistance(getSouth(coorList), end)
    if 0 <= getEast(coorList)[1] < len(arr) and (
            arr[coorList[0]][getEast(coorList)[1]] is None or arr[coorList[0]][getEast(coorList)[1]] == 'T'):
        e = getDistance(getEast(coorList), end)
    if 0 <= getWest(coorList)[1] < len(arr) and (
            arr[coorList[0]][getWest(coorList)[1]] is None or arr[coorList[0]][getWest(coorList)[1]] == 'T'):
        w = getDistance(getWest(coorList), end)

    newList = [n, s, e, w]
    min_dis = min(n, s, e, w)

    if min_dis == 1000:
        return None,None
    direction = [0, 0, 0, 0]
    direction2 = [0, 0, 0, 0]
    if newList.count(min_dis) > 1:
        print("Two Ways possible")
        index = newList.index(min_dis, 0, 4)
        direction[index] = 1
        newList.reverse()
        index2 = 3-newList.index(min_dis, 0, 4)
        direction2[index2] = 1
        return direction, direction2

    index = newList.index(min_dis, 0, 4)
    direction = [0, 0, 0, 0]
    direction[index] = 1
    if direction == [0,0,0,0]:
        return None,None
    return direction, None


def makeMove(arr, currentList,move):
    if arr[currentList[0]][currentList[1]] != 'A':
        arr[currentList[0]][currentList[1]] = 2
        arr[currentList[0]][currentList[1]] = '(////)'
    if move == [1, 0, 0, 0]:
        currentList = getNorth(currentList)
    elif move == [0, 1, 0, 0]:
        currentList = getSouth(currentList)
    elif move == [0, 0, 1, 0]:
        currentList = getEast(currentList)
    elif move == [0, 0, 0, 1]:
        currentList = getWest(currentList)
    return currentList


def solve(arr, currentList, stack):

    printGrid(arr)
    if currentList == endList:
        print("END NOW REACHED")
        return stack

    move, move2 = findBestMove(arr, currentList)

    if move != None and move2 != None:

        copyarr = copy.deepcopy(arr)
        stack.append(currentList)
        stackcopy = copy.copy(stack)
        minStack =  min(solve(copyarr,makeMove(copyarr,currentList,move),stackcopy),solve(copyarr,makeMove(copyarr,currentList,move2),stackcopy))
        print (minStack)
        return minStack

    if move != None:
        # directionGrid[currentList[0]][currentList[1]] = Directions(move)
        stack.append(currentList)
        return solve(arr,makeMove(arr,currentList,move),stack)
    else:
        if (len(stack) == 0):
            print(" NO SOLUTION ")
            return None
        else:
            prev = stack.pop()
            arr[currentList[0]][currentList[1]] = -2
            currentList = prev
            return solve(arr, currentList, stack)

if __name__ == '__main__':
    sizeOfGrid = 10
    arr = makeSquareGrid(sizeOfGrid)
    arr = fillGrid(arr)


    directionGrid = makeSquareGrid(sizeOfGrid)
    printGrid(arr)
    current = start
    stack = []
    currentList = list(current)
    endList = list(end)
    stack = solve(arr, currentList, stack)
    # printGrid(arr)
    printGrid(arr)
    print(stack)
