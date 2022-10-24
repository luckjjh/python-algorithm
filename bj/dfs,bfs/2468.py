import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    rMap = [list(map(int, readl().split())) for _ in range(N)]
    return N, rMap


N, rMap = Input_Data()


def Solve(row, col, h):
    q = deque()
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q.append((row, col))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow + r_d, curCol + c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            if rMap[nextRow][nextCol] < h:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))


maxCnt = -1

for h in range(max(map(max, rMap))+1):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if rMap[i][j] >= h and not visit[i][j]:
                Solve(i, j, h)
                cnt += 1
    maxCnt = max(cnt, maxCnt)
print(maxCnt)
