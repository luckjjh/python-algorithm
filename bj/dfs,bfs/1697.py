import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    return N, K


N, K = Input_Data()


def Solve():
    q = deque()
    q.append((N, 0))
    visit = [0]*100001
    while True:
        curDir, curTime = q.popleft()
        if curDir == K:
            print(curTime)
            return
        nextR = curDir+1
        nextL = curDir-1
        nextTele = curDir*2
        if 0 <= nextR <= 100000 and not visit[nextR]:
            visit[nextR] = 1
            q.append((nextR, curTime+1))
        if 0 <= nextL <= 100000 and not visit[nextL]:
            visit[nextL] = 1
            q.append((nextL, curTime+1))
        if 0 <= nextTele <= 100000 and not visit[nextTele]:
            visit[nextTele] = 1
            q.append((nextTele, curTime+1))


Solve()
