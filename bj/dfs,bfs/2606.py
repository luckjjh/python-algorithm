import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    M = int(readl())
    nList = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, nList


N, M, nList = Input_Data()
nMap = [[0]*(N+1) for _ in range(N+1)]
cnt = 0


def Solve():
    global cnt
    for row, col in nList:
        nMap[row][col] = 1
        nMap[col][row] = 1
    visit = [0]*(N+1)
    visit[1] = 1
    q = deque()
    q.append(1)
    while q:
        curDir = q.popleft()
        for i in range(1, N+1):
            if visit[i] == 1:
                continue
            if nMap[curDir][i]:
                visit[i] = 1
                q.append(i)
                cnt += 1

    print(cnt)


Solve()
