import sys
from collections import deque
# 해마다 열리는 꿀꿀이 올림피아드에는 여러 종목들이 있는데, 요즘에는 꿀꿀이들의 교양을 겨루는 ‘미술관람 대회’가 인기를 끌고 있다.
# 이 대회는 사회자가 빨강, 초록, 파랑으로 이루어진 N × N 픽셀의 그림을 보여주면 그 그림에 포함된 영역의 수를 빠르고 정확하게 맞추는 것이 목표이다.
# 동일한 색깔이 네 방향(상, 하, 좌, 우) 중 한 곳이라도 연결되어 있으면 하나의 영역으로 간주한다.

# 예를 들어, 아래 그림은 각각 2, 1, 1개의 빨간색, 초록색, 파란색 영역이 있어 총 4개의 영역이 있다.

# 한편, 꿀꿀이들의 절반 정도는 선천적인 유전자 때문에 적록색맹이라서 빨간색과 초록색을 구별하지 못한다.
# 따라서 사회자는 일반 대회와 적록색맹용 대회를 따로 만들어서 대회를 진행하려고 한다. 사회자를 도와 영역의 수를 구하는 프로그램을 작성하여라.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    gMap = [list(map(str, list(readl().rstrip()))) for _ in range(N)]
    return N, gMap


N, gMap = Input_Data()


def UnionRG():
    for i in range(N):
        for j in range(N):
            if gMap[i][j] == 'R':
                gMap[i][j] = 'G'
    return


def Solve(row, col):
    q = deque()
    curColor = gMap[row][col]
    q.append((row, col))
    visit[row][col] = 1
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if gMap[nextRow][nextCol] != curColor:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))


commonCnt = 0
rgCnt = 0
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            Solve(i, j)
            commonCnt += 1

UnionRG()
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            Solve(i, j)
            rgCnt += 1

print(commonCnt, rgCnt)
