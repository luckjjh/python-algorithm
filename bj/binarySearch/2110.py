import sys
from collections import deque
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N, C = map(int, readl().split())
    hList = [int(readl()) for _ in range(N)]
    return N, C, hList


N, C, hList = Input_Data()

hList.sort()

s = 1
e = hList[-1]-hList[0]
result = 0


def Solve(s, e):
    global result
    while s <= e:
        mid = (s+e)//2
        cur = hList[0]
        cnt = 1
        for i in range(1, len(hList)):
            if hList[i] >= cur+mid:
                cur = hList[i]
                cnt += 1
        if cnt >= C:
            s = mid+1
            result = mid
        else:
            e = mid-1


Solve(s, e)
print(result)
