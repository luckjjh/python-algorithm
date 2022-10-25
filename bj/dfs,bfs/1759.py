import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    L, C = map(int, readl().split())
    alist = list(map(str, readl().split()))
    return L, C, alist


L, C, alist = Input_Data()
ans = []
temp = ''
alist.sort()
consonant = ['a', 'e', 'o', 'i', 'u']


def Solve(level, cnt):
    global temp
    if level == L:
        vo, co = 0, 0
        for i in temp:
            if i in consonant:
                co += 1
            else:
                vo += 1
        if co < 1:
            return
        if vo < 2:
            return
        print(temp)
        return
    else:
        for i in range(cnt, C):
            temp += alist[i]
            Solve(level+1, i+1)
            temp = temp[:-1]


Solve(0, 0)
