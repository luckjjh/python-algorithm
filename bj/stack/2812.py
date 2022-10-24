import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    nums = list(map(int, list(readl().rstrip())))
    return N, K, nums


N, K, nums = Input_Data()


def Solve():
    cnt = 0
    stack = deque()
    for num in nums:
        if stack:
            if stack[-1] >= num or cnt == K:
                stack.append(num)
            else:
                while stack and stack[-1] < num and cnt < K:
                    cnt += 1
                    stack.pop()
                stack.append(num)
        else:
            stack.append(num)
    while len(stack) > (N-K):
        stack.pop()
    print(*stack, sep='')


Solve()
