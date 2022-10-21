from collections import deque
import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    cList = [int(readl()) for _ in range(N)]
    return N, cList


N, cList = Input_Data()


def Solve():
    stack = deque()
    cnt = 0
    for item in cList:
        if stack:
            if stack[-1] > item:
                cnt += len(stack)
                stack.append(item)
            else:
                while stack and stack[-1] <= item:
                    stack.pop()
                cnt += len(stack)
                stack.append(item)
        else:
            stack.append(item)
    print(cnt)


Solve()
