import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nums = list(map(int, readl().split()))
    return N, nums


N, nums = Input_Data()
memo = [-(sys.maxsize)]


def Solve():
    for i in nums:
        if memo[-1] < i:
            memo.append(i)
        else:
            left = 0
            right = len(memo)
            while left < right:
                mid = (left+right)//2
                if memo[mid] < i:
                    left = mid+1
                else:
                    right = mid
            memo[right] = i

    print(len(memo)-1)


Solve()
