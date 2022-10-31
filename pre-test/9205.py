import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    homeRow, homeCol = map(int, readl().split())
    cAxis = [list(map(int, readl().split())) for _ in range(N)]
    festRow, festCol = map(int, readl().split())
    return N, homeRow, homeCol, cAxis, festRow, festCol


def Solve():
    q = deque()
    q.append((homeRow, homeCol))
    while q:
        curRow, curCol = q.popleft()
        if abs(curRow-festRow)+abs(curCol-festCol) <= 1000:
            print("happy")
            return
        for i in range(N):
            if not visit[i]:
                nextRow, nextCol = cAxis[i]
                if abs(curRow-nextRow)+abs(curCol-nextCol) <= 1000:
                    q.append((nextRow, nextCol))
                    visit[i] = 1
    print("sad")
    return


testCase = int(sys.stdin.readline())

for _ in range(testCase):
    N, homeRow, homeCol, cAxis, festRow, festCol = Input_Data()
    visit = [0]*N
    Solve()
