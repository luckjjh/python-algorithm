import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    strList = list(map(str, list(readl().rstrip())))
    boom = str(readl())
    return strList, boom


strList, boom = Input_Data()


def Check():
    it = list(boom.strip())
    it.reverse()
    idx = -1
    for i in it:
        if i != stack[idx]:
            return False
        idx -= 1
    return True


stack = deque()


def Solve():
    for li in strList:
        stack.append(li)
        if len(stack) >= (len(boom)-1):
            if Check():
                for _ in range(len(boom)-1):
                    stack.pop()
    if stack:
        print(*stack, sep='')
    else:
        print('FRULA')


Solve()
