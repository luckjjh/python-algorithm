import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()
ans = [-1]*N


def Solve():
    stack = deque()
    for idx, num in enumerate(nums):
        if stack:
            if stack[-1][0] >= num:
                stack.append((num, idx))
            else:
                while stack and stack[-1][0] < num:
                    curNum, curIdx = stack.pop()
                    ans[curIdx] = num
                stack.append((num, idx))
        else:
            stack.append((num, idx))
    print(*ans)


Solve()
