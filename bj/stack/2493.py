import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()
ans = [0]*N


def Solve():
    stack = deque()
    for idx, item in enumerate(nums):
        if stack:
            while stack and stack[-1][1] <= item:
                stack.pop()

            if stack and stack[-1][1] > item:
                ans[idx] = stack[-1][0]+1
            stack.append((idx, item))
        else:
            stack.append((idx, item))
    print(*ans)


Solve()
