import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()


def Solve():
    temp = [0]*1000001
    ans = [-1]*(N)
    for num in nums:
        temp[num] += 1
    stack = deque()
    for idx, num in enumerate(nums):
        if stack:
            if stack[-1][1] >= temp[num]:
                stack.append((idx, temp[num]))
            else:
                while stack and stack[-1][1] < temp[num]:
                    popNum = stack.pop()
                    ans[popNum[0]] = num
                stack.append((idx, temp[num]))
        else:
            stack.append((idx, temp[num]))

    print(*ans)


Solve()
