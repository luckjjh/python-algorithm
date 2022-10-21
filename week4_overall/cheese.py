from pydoc import visiblename
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    Row, Col = map(int, readl().split())
    cMap = [list(map(int, readl().split())) for _ in range(Row)]
    return Row, Col, cMap


Row, Col, cMap = Input_Data()


def Check():
    cnt = 0
    for i in range(Row):
        for j in range(Col):
            if cMap[i][j] == 1:
                cnt += 1
    return cnt


def Solve():
    q = deque()
    q.append((0, 0))
    visit[0][0] = 1
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= Row or nextCol >= Col:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            if cMap[nextRow][nextCol] == 1:
                cMap[nextRow][nextCol] = 0
                continue
            q.append((nextRow, nextCol))


def Run():
    global visit
    cnt = 0
    lastCheese = 0
    while Check():
        lastCheese = Check()
        visit = [[0]*Col for _ in range(Row)]
        Solve()
        cnt += 1
    print(cnt)
    print(lastCheese)


Run()
