import sys
import bisect
# KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다.
# 사냥터에 온 사냥꾼은 일직선상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다.

# 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ... xM 은 x-좌표 값이라고 하자.

# 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN) 과 같이 x, y-좌표 값으로 표시하자. 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.

# 사냥꾼이 가지고 있는 총의 사정거리가 L 이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다.

# 단, 사대의 위치 xi와 동물의 위치 (aj,bj) 간의 거리는 |xi-aj| + bj 로 계산한다.

# 예를 들어, 아래의 그림과 같은 사냥터를 생각해보자.

# (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 사정거리 L이 4라고하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.

# 사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

# L - bj >= xi-aj


def Input_Data():
    readl = sys.stdin.readline
    M, N, L = map(int, readl().split())
    hList = list(map(int, readl().split()))
    aList = [list(map(int, readl().split())) for _ in range(N)]
    return M, N, L, hList, aList


M, N, L, hList, aList = Input_Data()

cnt = 0


def Solve():
    global cnt
    hList.sort()
    for x, y in aList:
        if y > L:
            continue
        low = x - (L-y)
        high = x + (L-y)
        idx = bisect.bisect_left(hList, low)
        if idx >= M or hList[idx] > high:
            continue
        cnt += 1
    print(cnt)


Solve()
