import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    maps = [list(map(int, readl().rstrip())) for _ in range(M)]
    return N, M, maps


N, M, maps = Input_Data()


def Solve():
    q = deque()
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q.append((0, 0))
    dist = [[-1] * N for _ in range(M)]
    dist[0][0] = 0
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= M or nextCol >= N:
                continue
            if dist[nextRow][nextCol] == -1:
                if maps[nextRow][nextCol] == 1:
                    dist[nextRow][nextCol] = dist[curRow][curCol]+1
                    q.append((nextRow, nextCol))
                if maps[nextRow][nextCol] == 0:
                    dist[nextRow][nextCol] = dist[curRow][curCol]
                    q.appendleft((nextRow, nextCol))
    print(dist[M-1][N-1])


Solve()
