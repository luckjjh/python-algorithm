import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    axisList = [list(map(int, (readl().split()))) for _ in range(N)]
    return N, axisList


N, axisList = Input_Data()
maps = [[0]*101 for _ in range(101)]


def Solve():
    for row, col in axisList:
        for i in range(10):
            for j in range(10):
                maps[row+i][col+j] = 1

    cnt = 0

    for i in maps:
        for j in i:
            if j == 1:
                cnt += 1

    print(cnt)


Solve()
