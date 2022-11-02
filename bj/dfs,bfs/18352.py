import sys
import heapq


def Input_Data():
    readl = sys.stdin.readline
    N, M, K, X = map(int, readl().split())
    aList = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, readl().split())
        aList[A-1].append((1, B-1))
    return N, M, K, X-1, aList


N, M, K, X, aList = Input_Data()


def Solve():
    dist = [987654321]*N
    dist[X] = 0
    pq = []
    heapq.heappush(pq, (0, X))
    while pq:
        curCost, curV = heapq.heappop(pq)
        for nextCost, nextV in aList[curV]:
            if nextCost+curCost < dist[nextV]:
                dist[nextV] = nextCost+curCost
                heapq.heappush(pq, (nextCost+curCost, nextV))
    ans = []
    for idx, item in enumerate(dist, 1):
        if item == K:
            ans.append(idx)

    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i)


Solve()
