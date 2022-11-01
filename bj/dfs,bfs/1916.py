import sys
import heapq


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    M = int(readl())
    cList = [[] for _ in range(N)]
    for _ in range(M):
        A, B, Cost = map(int, readl().split())
        cList[A-1].append((B-1, Cost))
    start, end = map(int, readl().split())
    return N, M, cList, start-1, end-1


N, M, cList, start, end = Input_Data()

dist = [987654321]*N


def Solve():
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    while pq:
        curCost, curV = heapq.heappop(pq)
        if curCost > dist[curV]:
            continue
        for nextV, nextCost in cList[curV]:
            if nextCost+curCost < dist[nextV]:
                dist[nextV] = nextCost+curCost
                heapq.heappush(pq, (nextCost+curCost, nextV))
    print(dist[end])


Solve()
