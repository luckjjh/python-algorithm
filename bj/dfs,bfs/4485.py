import sys
from collections import deque


def Solve():
    dist = [[sys.maxsize]*N for _ in range(N)]
    dist[0][0] = maps[0][0]
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    q.append((0, 0))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if dist[nextRow][nextCol] <= dist[curRow][curCol]+maps[nextRow][nextCol]:
                continue
            dist[nextRow][nextCol] = dist[curRow][curCol] + \
                maps[nextRow][nextCol]
            q.append((nextRow, nextCol))

    print("Problem", str(cnt)+":", dist[N-1][N-1])


def Run():
    global maps, N, cnt
    cnt = 1
    while True:
        readl = sys.stdin.readline
        N = int(readl())
        if not N:
            break
        maps = [list(map(int, readl().split())) for _ in range(N)]
        Solve()
        cnt += 1


Run()
