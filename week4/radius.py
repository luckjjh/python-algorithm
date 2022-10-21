import sys
from collections import deque
from time import gmtime
# 농부 존은 그의 들판에 N(1≤N≤10,000)개의 건초 더미를 놓으려 한다.
# 들판은 1*1 크기의 사각형으로 구성된 100*100 크기이고, 건초 더미들은 각각 1*1 크기의 사각형 한 칸을 차지한다. (한 칸에 두 개의 건초 더미가 놓이는 일은 없다)

# 농부 존은 건초 더미로 연결된 다양한 형태의 하나의 큰 영역이 생기는 것을 알았다.
#  즉, 건초 더미들 모두 인접한 (동서남북으로 한 칸) 곳에 다른 건초 더미가 있다. 한 건초 더미에서 출발해서 다른 모든 건초 더미에 도달할 수 있다. 건초 더미로 연결된 영역은 “구멍”을 포함하고 있다. 구멍은 건초 더미로 완전히 둘러싸인 빈 영역이다.

# 농부 존이 건초 베일에 의해 형성되는 영역의 둘레를 계산하는 것을 도와주시오.
# “구멍”은 둘레에 영향을 주지 않는다.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    hList = [list(map(int, readl().split())) for _ in range(N)]
    return N, hList


N, hList = Input_Data()


def Solve():
    hMap = [[0]*(102) for _ in range(102)]
    visit = [[0]*(102) for _ in range(102)]
    for item in hList:
        hMap[item[0]][item[1]] = 1
    q = deque()
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    cnt = 0
    q.append((0, 0))
    visit[0][0] = 1
    while q:
        curRow, curCol = q.popleft()
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow > 101 or nextCol > 101:
                continue
            if hMap[nextRow][nextCol] == 1:
                cnt += 1

            if hMap[nextRow][nextCol] == 0:
                if visit[nextRow][nextCol] == 1:
                    continue
                visit[nextRow][nextCol] = 1
                q.append((nextRow, nextCol))
    print(cnt)


Solve()
