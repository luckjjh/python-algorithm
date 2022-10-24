import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    aMap = [list(map(int, list(readl().rstrip()))) for _ in range(N)]
    return N, aMap


N, aMap = Input_Data()
ans = []


def Solve(row, col):
    curCnt = 1
    q = deque()
    q.append((row, col))
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if aMap[nextRow][nextCol] == 0:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))
            curCnt += 1
    ans.append(curCnt)


cnt = 0

visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if aMap[i][j] and not visit[i][j]:
            visit[i][j] = 1
            Solve(i, j)
            cnt += 1
print(cnt)
ans.sort()
for i in ans:
    print(i)
