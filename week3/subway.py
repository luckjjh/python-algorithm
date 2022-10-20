import sys
from collections import deque
import heapq
# 지방에서 서울에 관광 온 성수는 지하철 노선을 보고 깜짝 놀랐다.
# 노선이 엄청나게 복잡하기 때문이었다. 각 노선들이 서로 얽혀있어서 잘못하면 10분도 안 걸리는 거리를 1시간 동안 갈 수도 있는 상황이었다.
# 어쩔 수 없이 성수는 현재 숙소에서 관광할 목적지까지 가장 짧은 시간에 도착할 수 있는 경로와 시간을 표로 만들려고 한다.

# 단, 각 지하철역에서 관광지가 있고, 지하철을 갈아타는데 소요되는 시간은 없다고 가정한다.


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    sMap = [list(map(int, readl().split())) for _ in range(N)]
    return N, M, sMap


N, M, sMap = Input_Data()

dir = [987654321]*N


def Solve():
    dir[0] = 0
    nearest = [0]*N
    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        curCost, curV = heapq.heappop(pq)
        for nextV, nextCost in enumerate(sMap[curV]):
            if dir[nextV] > curCost+nextCost:
                dir[nextV] = curCost+nextCost
                nearest[nextV] = curV
                heapq.heappush(pq, (nextCost+curCost, nextV))

    print(dir[M-1])

    ans = []
    end = M-1
    while 0 != end:
        ans.append(end)
        end = nearest[end]
    ans.append(0)
    route = []
    for item in ans:
        route.append(item+1)
    route.reverse()
    print(*route)


Solve()
