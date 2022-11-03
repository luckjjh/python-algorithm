import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    bList = [int(readl()) for _ in range(N)]
    return N, bList


N, bList = Input_Data()


def Solve():
    stack = deque()
    cnt = 0
    for item in bList:
        while stack and stack[-1] <= item:
            stack.pop()
        cnt += len(stack)
        stack.append(item)
    print(cnt)


Solve()
