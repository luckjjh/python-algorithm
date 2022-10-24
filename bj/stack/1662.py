from curses.ascii import isdigit
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    cList = list(map(str, list(readl().rstrip())))
    return cList


cList = Input_Data()
ans = 0


def Solve():
    global ans
    stack = deque()
    for cmd in cList:
        if cmd.isdigit():
            ans += 1
            temp = cmd
        elif cmd == '(':
            stack.append((temp, ans-1))
            ans = 0
        else:
            multi, preL = stack.pop()
            ans = (int(multi)*ans)+preL
    print(ans)


Solve()
