import sys
from itertools import combinations


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M


N, M = Input_Data()


def Solve():
    arr = []
    for i in range(1, N+1):
        arr.append(i)
    ans = list(combinations(arr, M))
    for i in ans:
        print(*i)


Solve()
