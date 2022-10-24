import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    M, N, K = map(int, readl().split())
    bList = [list(map(int, readl().split())) for _ in range(K)]
    return N, M, K, bList


def Solve(row, col):
    q = deque()
    q.append((row, col))
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= M:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            if bMap[nextRow][nextCol] == 0:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))


testCase = int(sys.stdin.readline())
for _ in range(testCase):
    N, M, K, bList = Input_Data()
    bMap = [[0]*M for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    for r, c in bList:
        bMap[c][r] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if bMap[i][j] == 1 and not visit[i][j]:
                Solve(i, j)
                cnt += 1

    print(cnt)
