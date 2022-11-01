import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    liquid = list(map(int, readl().split()))
    return N, liquid


N, liquid = Input_Data()

liquid.sort()
ans = sys.maxsize
left = 0
right = N-1
result = []


def Solve():
    global result, left, right, ans
    while left < right:
        leftI = liquid[left]
        rightI = liquid[right]

        total = leftI+rightI
        if abs(total) < ans:
            ans = abs(total)
            result = [leftI, rightI]

        if total < 0:
            left += 1
        else:
            right -= 1
    print(*result)


Solve()
