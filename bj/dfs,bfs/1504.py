import sys
import heapq
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, E = map(int, readl().split())
    aList = [[] for _ in range(N)]
    for _ in range(E):
        A, B, Cost = map(int, readl().split())
        aList[A-1].append((B-1, Cost))
        aList[B-1].append((A-1, Cost))
    v1, v2 = map(int, readl().split())
    return N, E, aList, v1-1, v2-1


N, E, aList, v1, v2 = Input_Data()


def Solve(start):
    pq = []
    dist = [sys.maxsize]*N
    dist[start] = 0
    heapq.heappush(pq, (0, start))
    while pq:
        curCost, curDir = heapq.heappop(pq)
        for nextDir, nextCost in aList[curDir]:
            if curCost+nextCost < dist[nextDir]:
                dist[nextDir] = curCost+nextCost
                heapq.heappush(pq, (curCost+nextCost, nextDir))

    return dist


list0 = Solve(0)
list1 = Solve(v1)
list2 = Solve(v2)
minCost = min(list0[v1]+list1[v2]+list2[N-1], list0[v2]+list2[v1]+list1[N-1])
if minCost >= sys.maxsize:
    print(-1)
else:
    print(minCost)
