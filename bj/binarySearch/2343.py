import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    nums = list(map(int, readl().split()))
    return N, M, nums


N, M, nums = Input_Data()
result = sum(nums)


def Solve():
    global result
    low = 0
    high = sys.maxsize
    while low <= high:
        mid = (high+low)//2
        if mid < max(nums):
            low = mid+1
            continue
        cnt, temp = 1, 0
        for i in range(len(nums)):
            if temp+nums[i] <= mid:
                temp += nums[i]
            else:
                temp = nums[i]
                cnt += 1
        if cnt <= M:
            high = mid-1
            result = min(result, mid)
        else:
            low = mid+1

    print(result)


Solve()
