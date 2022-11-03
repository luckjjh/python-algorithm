import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    return N, K


N, K = Input_Data()


def Solve():
    q = deque()
    visit = [0]*100001
    visit[N] = 1
    q.append((N, 0))
    while q:
        curDir, curTime = q.popleft()
        if curDir == K:
            print(curTime)
            return
        nextDir = curDir+1
        nextTele = curDir*2
        prevDir = curDir-1
        if 0 <= nextDir <= 100000 and not visit[nextDir]:
            visit[nextDir] = 1
            q.append((nextDir, curTime+1))
        if 0 <= prevDir <= 100000 and not visit[prevDir]:
            visit[prevDir] = 1
            q.append((prevDir, curTime+1))
        if 0 <= nextTele <= 100000 and not visit[nextTele]:
            visit[nextTele] = 1
            q.append((nextTele, curTime+1))


Solve()
