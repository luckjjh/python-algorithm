import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    sMap = [list(map(int, list(readl().rstrip()))) for _ in range(N)]
    return N, sMap


N, sMap = Input_Data()
visit = [[0]*N for _ in range(N)]


def Solve(row, col):
    q = deque()
    dir = ((-1, 0), (-1, 1), (0, 1), (1, 1),
           (1, 0), (1, -1), (0, -1), (-1, -1))
    visit[row][col] = 1
    q.append((row, col))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if sMap[nextRow][nextCol] == 0:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))


cnt = 0
for i in range(N):
    for j in range(N):
        if sMap[i][j] == 1 and visit[i][j] == 0:
            Solve(i, j)
            cnt += 1
print(cnt)
