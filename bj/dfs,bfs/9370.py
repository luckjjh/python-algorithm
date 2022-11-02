import sys
import heapq


def Input_Data():
    readl = sys.stdin.readline
    N, M, T = map(int, readl().split())
    S, G, H = map(int, readl().split())
    aList = [[] for _ in range(N)]
    for _ in range(M):
        A, B, Cost = map(int, readl().split())
        if (A == G and B == H) or (A == H and B == G):
            ghCost = Cost
        aList[A-1].append((Cost, B-1))
        aList[B-1].append((Cost, A-1))
    candiList = [int(readl()) for _ in range(T)]
    candiList = map(lambda i: i-1, candiList)
    return N, M, T, S-1, G-1, H-1, aList, candiList, ghCost


def Dijkstra(start):
    dist = [987654321]*N
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        curCost, curV = heapq.heappop(pq)
        for nextCost, nextV in aList[curV]:
            if nextCost+curCost < dist[nextV]:
                dist[nextV] = nextCost+curCost
                heapq.heappush(pq, (nextCost+curCost, nextV))
    return dist


def Solve():
    origin = Dijkstra(S)
    toG = Dijkstra(G)
    toH = Dijkstra(H)
    ans = []
    for item in candiList:
        if origin[item] == toG[S]+toH[item]+ghCost:
            ans.append(item)
        if origin[item] == toH[S]+toG[item]+ghCost:
            ans.append(item)
    ans.sort()
    ans = map(lambda i: i+1, ans)
    print(*ans)


testCase = int(sys.stdin.readline())
for _ in range(testCase):
    N, M, T, S, G, H, aList, candiList, ghCost = Input_Data()
    Solve()
