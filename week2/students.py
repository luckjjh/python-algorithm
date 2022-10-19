import sys

# lambda, 정렬 메소드 parameter 정리 필요


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    sList = map(int, readl().split())
    scoreList = [[s, i] for i, s in enumerate(sList, 1)]
    return N, scoreList


N, scoreList = Input_Data()


def Solve():
    scoreList.sort(key=lambda x: (-x[0], x[1]))
    ans = [scoreList[i][1] for i in range(3)]
    print(*ans)


Solve()
