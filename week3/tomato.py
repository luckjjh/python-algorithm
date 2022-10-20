import sys
from collections import deque
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며,
# 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.


def Input_Data():
    readl = sys.stdin.readline
    Col, Row = map(int, readl().split())
    tMap = [list(map(int, readl().split())) for _ in range(Row)]
    return Col, Row, tMap


Col, Row, tMap = Input_Data()


def Solve():
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q = deque()
    emptyCnt = 0
    for i in range(Row):
        for j in range(Col):
            if tMap[i][j] == 1:
                q.append((i, j, 0))
            if tMap[i][j] == 0:
                emptyCnt += 1
    if emptyCnt == 0:
        print(0)
        return
    while q:
        curRow, curCol, curTime = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= Row or nextCol >= Col:
                continue
            if tMap[nextRow][nextCol] != 0:
                continue
            tMap[nextRow][nextCol] = 1
            q.append((nextRow, nextCol, curTime+1))
            emptyCnt -= 1

    if emptyCnt == 0:
        print(curTime)
    else:
        print(-1)
        return


Solve()
