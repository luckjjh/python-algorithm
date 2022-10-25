import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


N = Input_Data()

chess = [0]*N
cnt = 0


def Check(x):
    for i in range(x):
        if chess[x] == chess[i] or abs(chess[x]-chess[i]) == abs(x-i):
            return False
    return True


def Solve(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        chess[idx] = i
        if Check(idx):
            Solve(idx+1)


Solve(0)
print(cnt)
