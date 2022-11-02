import bisect
from itertools import combinations
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, S = map(int, readl().split())
    nums = list(map(int, readl().split()))
    return N, S, nums


N, S, nums = Input_Data()


def Solve():
    mid = len(nums)//2
    lista = nums[:mid]
    listb = nums[mid:]
    aSum = []
    bSum = []
    cnt = 0
    for i in range(1, len(lista)+1):
        for arr in list(combinations(lista, i)):
            aSum.append(sum(arr))

    for i in range(1, len(listb)+1):
        for arr in list(combinations(listb, i)):
            bSum.append(sum(arr))
    aSum.sort()
    bSum.sort()
    for i in aSum:
        need = S-i
        low = bisect.bisect_left(bSum, need)
        high = bisect.bisect_right(bSum, need)
        cnt += high-low
    for i in aSum:
        if S == i:
            cnt += 1
    for i in bSum:
        if S == i:
            cnt += 1
    print(cnt)


Solve()
