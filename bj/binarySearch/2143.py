import sys
import bisect
from itertools import combinations


def Input_Data():
    readl = sys.stdin.readline
    T = int(readl())
    n = int(readl())
    nnums = list(map(int, readl().split()))
    m = int(readl())
    mnums = list(map(int, readl().split()))
    return T, n, m, nnums, mnums


T, n, m, nnums, mnums = Input_Data()


def Solve():
    cnt = 0
    listA = []
    listB = []
    for i in range(len(nnums)):
        for j in range(i+1, len(nnums)+1):
            listA.append(sum(nnums[i:j]))
    for i in range(len(mnums)):
        for j in range(i+1, len(mnums)+1):
            listB.append(sum(mnums[i:j]))
    listA.sort()
    listB.sort()
    for i in listA:
        correct = T-i
        low = bisect.bisect_left(listB, correct)
        high = bisect.bisect_right(listB, correct)
        cnt += high-low

    print(cnt)


Solve()
