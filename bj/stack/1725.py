import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = [int(readl()) for _ in range(N)]
    return N, nums


N, nums = Input_Data()
ans = 0


def Solve():
    global ans
    stack = deque()
    for idx, num in enumerate(nums):
        while stack and nums[stack[-1]] > num:
            temp = stack.pop()

            if len(stack) == 0:
                width = idx
            else:
                width = idx-stack[-1]-1
            ans = max(ans, width*nums[temp])
        stack.append(idx)

    while stack:
        temp = stack.pop()
        if not stack:
            width = N
        else:
            width = N-stack[-1]-1
        ans = max(ans, width*nums[temp])
    print(ans)


Solve()
