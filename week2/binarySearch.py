import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    T = int(readl())
    findNums = list(map(int, readl().split()))
    return N, T, nums, findNums


N, T, nums, findNums = Input_Data()


def Solve():
    nums.sort()
    for i in findNums:
        idx = bisect.bisect_left(nums, i)
        if nums[idx] == i:
            print(idx+1)
        else:
            print(0)


Solve()
