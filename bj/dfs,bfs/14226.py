import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    S = int(readl())
    return S


S = Input_Data()


def Solve():
    check = dict()
    check[(1, 0)] = 0
    q = deque()
    q.append((1, 0))
    while q:
        curImogi, curClip = q.popleft()
        if curImogi == S:
            print(check[(curImogi, curClip)])
            return
        if (curImogi, curImogi) not in check.keys():
            check[(curImogi, curImogi)] = check[(curImogi, curClip)]+1
            q.append((curImogi, curImogi))
        if (curImogi+curClip, curClip) not in check.keys():
            check[(curImogi+curClip, curClip)] = check[(curImogi, curClip)]+1
            q.append((curImogi+curClip, curClip))
        if (curImogi-1, curClip) not in check.keys():
            check[(curImogi-1, curClip)] = check[(curImogi, curClip)]+1
            q.append((curImogi-1, curClip))


Solve()
