import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    kRow, kCol, eRow, eCol = map(int, readl().split())
    return N, M, kRow, kCol, eRow, eCol


N, M, kRow, kCol, eRow, eCol = Input_Data()
visit = [[0]*N for _ in range(M)]


def Solve():
    q = deque()
    q.append((kRow, kCol, 0))
    dir = ((-2, 1), (-1, 2), (1, 2), (2, 1),
           (2, -1), (1, -2), (-1, -2), (-2, -1))
    visit[kRow][kCol] = 1
    while q:
        curRow, curCol, curStep = q.popleft()
        if curRow == eRow and curCol == eCol:
            return curStep
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= M:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol, curStep+1))


print(Solve())
