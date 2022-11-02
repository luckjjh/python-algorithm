import sys
import bisect
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()
ans = [0]


def Solve():
    q = deque()
    for i in nums:
        if ans[-1] < i:
            ans.append(i)
        else:
            idx = bisect.bisect_left(ans, i)
            ans[idx] = i
    print(len(ans)-1)


Solve()
