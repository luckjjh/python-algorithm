import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    M = int(readl())
    findNums = list(map(int, readl().split()))
    return N, M, nums, findNums


N, M, nums, findNums = Input_Data()

ans = []


def Solve():
    for i in findNums:
        low = bisect.bisect_left(nums, i)
        high = bisect.bisect_right(nums, i)
        ans.append(high-low)


Solve()
print(*ans)
