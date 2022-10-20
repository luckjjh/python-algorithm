import sys
from collections import deque
from termios import VSUSP
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    aMap = [list(map(int, list(readl().rstrip()))) for _ in range(N)]
    return N, aMap


N, aMap = Input_Data()
visit = [[0]*N for _ in range(N)]
cnt = 0


def Solve(row, col):
    q = deque()
    curCnt = 1
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
            if aMap[nextRow][nextCol] == 0:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            q.append((nextRow, nextCol))
            curCnt += 1
    return curCnt


ans = []
for i in range(N):
    for j in range(N):
        if aMap[i][j] == 1 and visit[i][j] == 0:
            ans.append(Solve(i, j))
            cnt += 1
print(cnt)
ans.sort()
for i in ans:
    print(i)
