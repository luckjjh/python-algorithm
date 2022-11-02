from os import curdir
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    return N, K


N, K = Input_Data()

minCost = sys.maxsize


def Solve():
    q = deque()
    q.append((N, 0))
    visit = [0]*100001
    dist = [-1]*100001
    dist[N] = 0
    visit[N] = 1
    while q:
        curDir, curCost = q.popleft()
        if curDir*2 <= 100000 and not visit[curDir*2]:
            q.appendleft((curDir*2, curCost))
            visit[curDir*2] = 1
            dist[curDir*2] = dist[curDir]
        if curDir+1 <= 100000 and not visit[curDir+1]:
            q.append((curDir+1, curCost+1))
            visit[curDir+1] = 1
            dist[curDir+1] = dist[curDir]+1
        if curDir-1 >= 0 and not visit[curDir-1]:
            q.append((curDir-1, curCost+1))
            visit[curDir-1] = 1
            dist[curDir-1] = dist[curDir]+1

    print(dist[K])


Solve()
