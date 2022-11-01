import sys
import bisect
from collections import deque
import heapq


def Input_Data():
    curMax = -1
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    adjMap = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, readl().split())
        adjMap[A-1].append((B-1, C))
        adjMap[B-1].append((A-1, C))
        curMax = max(C, curMax)
    fA, fB = map(int, readl().split())
    return N, M, fA-1, fB-1, adjMap, curMax


N, M, fA, fB, adjMap, curMax = Input_Data()


def BFS():
    visited[fA] = 1
    q = deque()
    q.append(fA)
    while q:
        curV = q.popleft()
        if curV == fB:
            return True
        for nx, nc in adjMap[curV]:
            if visited[nx] == 0 and mid <= nc:
                q.append(nx)
                visited[nx] = 1
    return False


def Solve():
    start = 1
    end = curMax
    while start <= end:
        global mid
        mid = (start+end)//2
        global visited
        visited = [0]*N
        if BFS():
            start = mid+1
        else:
            end = mid-1
    print(end)


Solve()
