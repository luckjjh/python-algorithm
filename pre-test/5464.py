import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    cost = [int(readl()) for _ in range(N)]
    weight = [int(readl()) for _ in range(M)]
    inOut = [int(readl()) for _ in range(2*M)]
    return N, M, cost, weight, inOut


N, M, cost, weight, inOut = Input_Data()
parking = [0]*N
waiting = deque()


def Solve():
    ans = 0
    for cmd in inOut:
        if waiting:
            for i in range(N):
                if parking[i] == 0:
                    parking[i] = waiting.popleft()

        if cmd > 0:
            check = True
            for i in range(N):
                if parking[i] == 0:
                    parking[i] = cmd
                    check = False
                    break
            if check:
                waiting.append(cmd)

        else:
            for i in range(N):
                if parking[i] == (-cmd):
                    parking[i] = 0
                    curCost = weight[-cmd-1] * cost[i]
                    ans += curCost

    print(ans)


Solve()
