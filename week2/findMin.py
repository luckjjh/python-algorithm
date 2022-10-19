import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()


def Solve():
    nums.sort()
    print(*nums[:4])


Solve()
