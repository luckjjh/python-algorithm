import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    maps = [list(map(int, list(readl().rstrip()))) for _ in range(N)]
    return N, maps


N, maps = Input_Data()


def Solve():
    q = deque()
    dist = [[-1]*N for _ in range(N)]
    q.append((0, 0))
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    dist[0][0] = 0
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if dist[nextRow][nextCol] == -1:
                if maps[nextRow][nextCol] == 1:
                    dist[nextRow][nextCol] = dist[curRow][curCol]
                    q.appendleft((nextRow, nextCol))
                else:
                    dist[nextRow][nextCol] = dist[curRow][curCol]+1
                    q.append((nextRow, nextCol))
    print(dist[N-1][N-1])


Solve()
