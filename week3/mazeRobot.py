import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    Col, Row = map(int, readl().split())
    sCol, sRow, eCol, eRow = map(int, readl().split())
    mMap = [list(map(int, list(readl().rstrip()))) for _ in range(Row)]
    return Row, Col, sRow-1, sCol-1, eRow-1, eCol-1, mMap


Row, Col, sRow, sCol, eRow, eCol, mMap = Input_Data()
visit = [[0]*Col for _ in range(Row)]


def Solve():
    q = deque()
    q.append((sRow, sCol, 0))
    visit[sRow][sCol] = 1
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        curRow, curCol, curMove = q.popleft()
        if curRow == eRow and curCol == eCol:
            return curMove
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= Row or nextCol >= Col:
                continue
            if mMap[nextRow][nextCol] == 1:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol, curMove+1))
    return -1


print(Solve())
