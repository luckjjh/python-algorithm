import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    Col, Row, H = map(int, readl().split())
    tMap = [[list(map(int, readl().split())) for _ in range(Row)]
            for _ in range(H)]
    return Row, Col, H, tMap


Row, Col, H, tMap = Input_Data()


def Solve():
    tCnt = 0
    q = deque()
    for i in range(H):
        for j in range(Row):
            for k in range(Col):
                if tMap[i][j][k] == 1:
                    q.append((i, j, k, 0))
                if tMap[i][j][k] == 0:
                    tCnt += 1
    dir = ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0))
    if tCnt == 0:
        print(0)
        return
    while q:
        ch, crow, ccol, ccnt = q.popleft()
        for h_d, r_d, c_d in dir:
            nh, nrow, ncol = ch+h_d, crow+r_d, ccol+c_d
            if nh < 0 or nrow < 0 or ncol < 0:
                continue
            if nh >= H or nrow >= Row or ncol >= Col:
                continue
            if tMap[nh][nrow][ncol] == -1 or tMap[nh][nrow][ncol] == 1:
                continue
            tMap[nh][nrow][ncol] = 1
            tCnt -= 1
            q.append((nh, nrow, ncol, ccnt+1))
    if tCnt == 0:
        print(ccnt)
        return
    else:
        print(-1)
        return


Solve()
