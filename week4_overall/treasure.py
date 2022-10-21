from pydoc import visiblename
import sys
from collections import deque
# 보물섬 지도를 발견한 후크 선장은 보물을 찾아 나섰다. 보물섬 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다.
# 각 칸은 육지(L)나 바다(W)로 표시되어 있다. 이 지도에서 이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다.
# 보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다.
# 육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안된다.


def Input_Data():
    readl = sys.stdin.readline
    Row, Col = map(int, readl().split())
    tMap = [list(map(str, list(readl().rstrip()))) for _ in range(Row)]
    return Row, Col, tMap


Row, Col, tMap = Input_Data()


maxLen = -1


def Solve():
    for i in range(Row):
        for j in range(Col):
            if tMap[i][j] == 'L':
                global visit
                visit = [[0]*Col for _ in range(Row)]
                FindMax(i, j)
    print(maxLen)


def FindMax(row, col):
    global maxLen
    q = deque()
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    q.append((row, col, 0))
    visit[row][col] = 1
    while q:
        curRow, curCol, curMove = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= Row or nextCol >= Col:
                continue
            if tMap[nextRow][nextCol] == 'W':
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol, curMove+1))
    maxLen = max(curMove, maxLen)


Solve()
