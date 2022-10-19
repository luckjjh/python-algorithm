from re import T
import sys


def Input_Data():
    readl = sys.stdin.readline
    N = readl()
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()


def Solve():
    nums.sort(reverse=True)
    print(*nums)


Solve()
