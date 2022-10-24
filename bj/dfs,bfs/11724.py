import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    eList = [map(int, readl().split()) for _ in range(M)]
    return N, M, eList


N, M, eList = Input_Data()
cnt = 0


def Solve():
    global cnt
    eMap = [[0]*N for _ in range(N)]
    for r, c in eList:
        eMap[r-1][c-1] = 1
        eMap[c-1][r-1] = 1
    visit = [0]*N
    q = deque()
    for i in range(N):
        if visit[i] == 1:
            continue
        q.append(i)
        visit[i] = 1
        while q:
            curDir = q.popleft()
            for j in range(N):
                if visit[j] == 1:
                    continue
                if eMap[curDir][j] == 1:
                    visit[j] = 1
                    q.append(j)
        cnt += 1
    print(cnt)


Solve()
