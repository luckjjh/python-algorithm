import sys
import heapq


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    M = int(readl())
    pList = [[] for _ in range(N)]
    for _ in range(M):
        A, B, Cost = map(int, readl().split())
        pList[A-1].append((B-1, Cost))
    start, end = map(int, readl().split())
    return N, M, pList, start-1, end-1


N, M, pList, start, end = Input_Data()
dist = [987654321]*N


def Solve():
    global end
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0
    nearest = [0]*N
    while pq:
        curCost, curV = heapq.heappop(pq)
        if curCost > dist[curV]:
            continue
        for nextV, cost in pList[curV]:
            if cost+curCost < dist[nextV]:
                dist[nextV] = cost+curCost
                nearest[nextV] = curV
                heapq.heappush(pq, (cost+curCost, nextV))

    print(dist[end])
    tmp = end
    ans = []
    while start != end:
        temp = nearest[end]
        ans.append(temp)
        end = temp
    print(len(ans)+1)
    ans.reverse()
    ans.append(tmp)
    ans = map(lambda i: i+1, ans)
    print(*ans)


Solve()
