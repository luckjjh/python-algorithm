import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    cmd = list(readl())
    N = int(readl())
    temp = str(readl())
    if N == 0:
        nums = []
    else:
        temp = temp.rstrip()
        nums = list(temp[1:-1].split(','))
    return cmd, N, nums


def Solve():
    reverseNum = 0
    for i in cmd:
        if i == 'R':
            reverseNum += 1
        if i == 'D':
            if len(nums) == 0:
                print('error')
                return
            if reverseNum % 2 == 1:
                nums.pop(-1)
            else:
                nums.pop(0)
    if reverseNum % 2 == 1:
        nums.reverse()
    print('[', end='')
    print(*nums, sep=',', end='')
    print(']')


tc = int(sys.stdin.readline())

for _ in range(tc):
    cmd, N, nums = Input_Data()
    Solve()
