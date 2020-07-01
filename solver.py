import random


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
            check = False
    check = True
    while check:
        i = random.randint(0, row - 1)
        j = random.randint(0, row - 1)
        if arr[i][j] is None:
            arr[i][j] = 'T'
            check = False

    return arr


def printGrid(arr):

    s = [[str(e) for e in row] for row in arr]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


if __name__ == '__main__':
    arr = makeSquareGrid(10)
    arr = fillGrid(arr)
    printGrid(arr)
