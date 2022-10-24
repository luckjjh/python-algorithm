import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    Row, Col = map(int, readl().split())
    maze = [list(map(int, list(readl().rstrip()))) for _ in range(Row)]
    return Row, Col, maze


Row, Col, maze = Input_Data()


def Solve():
    q = deque()
    q.append((0, 0, 1))
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visit = [[0]*Col for _ in range(Row)]
    visit[0][0] = 1
    while q:
        curRow, curCol, curTime = q.popleft()
        if curRow == Row-1 and curCol == Col-1:
            print(curTime)
            return
        for r_d, c_d in dir:
            nextRow, nextCol = curRow + r_d, curCol + c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= Row or nextCol >= Col:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            if maze[nextRow][nextCol] == 0:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol, curTime+1))


Solve()
