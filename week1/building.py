import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    hList = [int(readl()) for _ in range(N)]
    return N, hList


N, hList = Input_Data()
ans = [0]*(N+1)


def Solve():
    stack = deque()
    for idx, height in enumerate(hList, 1):
        while stack and stack[-1][1] < height:
            temp = stack.pop()
            ans[temp[0]] = idx
        stack.append((idx, height))
    print(*ans[1:], sep='\n')


Solve()
