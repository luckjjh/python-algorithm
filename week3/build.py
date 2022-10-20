import sys
from telnetlib import BM
# (주)정올에서는 여러 개의 빌딩을 새로 지을 계획이다. 그래서 빌딩을 세울 장소를 선정하였다. 그리고 각 빌딩을 각 장소에 세울 경우에 드는 비용을 추정하였다. 예를 들어서 아래의 표를 보자

#              1 2 3
#            A 4 7 3
#            B 2 6 1
#            C 3 9 4

# A, B, C 는 건물을 나타내고, 1, 2, 3은 장소를 나타낸다. 예를 들어서 건물 B를 장소 1에 세우면 비용이 2가 들고, 장소 2에 세우면 비용이 6, 장소 3에 세우면 비용이 1만큼 든다. 물론 한 장소에는 한 건물밖에 세울 수 없다. 만일 A를 장소 2에, B를 장소 3에, C를 1에 세우면 전체 비용이 7+1+3 = 11이 필요하다. 그런데 A를 3, B를 1, C를 2에 세우면 3+2+9 = 14 가 필요하다.

# 각 빌딩을 어느 장소에 세우면 비용의 합이 최소가 되는지 구하는 프로그램을 작성하시오.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    bMap = [list(map(int, readl().split())) for _ in range(N)]
    return N, bMap


N, bMap = Input_Data()

minSum = 987654321
visit = [0]*N


def Check():
    for i in visit:
        if i == 0:
            return False
    return True


def Solve(idx, curSum):
    global minSum
    if curSum >= minSum:
        return
    if Check():
        minSum = min(curSum, minSum)
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        Solve(idx+1, curSum+bMap[idx][i])
        visit[i] = 0


Solve(0, 0)
print(minSum)
