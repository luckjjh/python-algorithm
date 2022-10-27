import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    aList = [list(map(int, readl().split())) for _ in range(N)]
    return N, aList


N, aList = Input_Data()
dMap = [[0]*101 for _ in range(101)]


def Solve():
    for row, col in aList:
        for i in range(0, 10):
            for j in range(0, 10):
                dMap[row+i][col+j] = 1
    cnt = 0
    for i in dMap:
        cnt += i.count(1)
    print(cnt)


Solve()
