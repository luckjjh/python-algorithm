import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pList = [int(readl()) for _ in range(N)]
    return N, pList


N, pList = Input_Data()


def Solve():
    cnt = 0
    stack = deque()
    for i in pList:
        while stack and stack[-1][0] < i:
            cnt += stack.pop()[1]

        if not stack:
            stack.append((i, 1))
            continue
        if stack[-1][0] == i:
            temp = stack.pop()[1]
            cnt += temp
            if stack:
                cnt += 1
            stack.append((i, temp+1))
        else:
            stack.append((i, 1))
            cnt += 1
    print(cnt)


Solve()
