import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    w, h = map(int, readl().split())
    return w, h


def Solve(row, col):
    q = deque()
    q.append((row, col))
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1),
           (-1, 1), (1, 1), (1, -1), (-1, -1))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= h or nextCol >= w:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            if iMap[nextRow][nextCol] == 0:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))


while True:
    w, h = Input_Data()
    if w == 0 and h == 0:
        break
    iMap = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if iMap[i][j] and not visit[i][j]:
                visit[i][j] = 1
                Solve(i, j)
                cnt += 1
    print(cnt)
