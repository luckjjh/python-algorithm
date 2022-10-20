
import sys
# 문제를 잘 풀기로 소문난 도경이는 모든 올림피아드 대회에 참가하고 싶어 했다.
# 대회에 참가하여 상이란 상은 다 타고 싶은 마음이었지만, 한 가지 걸리는 것이 있었다.

# 문제는 올림피아드 대회가 모두 해외에서 열리는 관계로 비행기 값이 굉장히 많이 들어간다는 것이다.
# 결국에는 집으로 다시 돌아와야 하는데, 모든 대회에 1번씩만 참가하고 집으로 돌아오는 경비를 가장 최소화하고 싶다.
# 도경이는 이것을 해결하지 못하면, 대회에 참가하기가 어렵게 된다.
# 대회는 참가하기만 하면 언제든지 알고리즘 문제를 풀 수 있기 때문에 경기를 계산하는 것 이외의 사항은 고려하지 않아도 된다.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    aMap = [list(map(int, readl().split())) for _ in range(N)]
    return N, aMap


N, aMap = Input_Data()

visit = [0]*N
visit[0] = 1
minCost = 987654321


def Check():
    for i in visit:
        if i == 0:
            return False
    return True


def Solve(curDir, curCost):
    global minCost
    if curCost >= minCost:
        return
    if Check() and aMap[curDir][0]:
        minCost = min(curCost+aMap[curDir][0], minCost)
        return
    for i in range(1, N):
        if visit[i] == 1:
            continue
        if aMap[curDir][i] == 0:
            continue
        visit[i] = 1
        nextCost = aMap[curDir][i]+curCost
        Solve(i, nextCost)
        visit[i] = 0


Solve(0, 0)
print(minCost)
