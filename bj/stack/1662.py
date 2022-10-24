import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    cList = list(map(str, list(readl().rstrip())))
    return cList


cList = Input_Data()


def Solve():
    stack = deque()
    for cmd in cList:
        if cmd == ')':
            q = deque()
            while stack and stack[-1] != '(':
                q.appendleft(stack.pop())
            stack.pop()
            N = stack.pop()
            for _ in range(int(N)):
                for j in q:
                    stack.append(j)
        else:
            stack.append(cmd)
    print(len(stack))


Solve()
