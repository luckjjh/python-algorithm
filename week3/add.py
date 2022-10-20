
import sys


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    nums = list(map(int, readl().split()))
    return N, K, nums


testCase = int(sys.stdin.readline())


def Solve(idx, sum):
    if sum == K:
        return True
    if sum > K:
        return False
    if idx >= N:
        return False

    if Solve(idx+1, sum+nums[idx]):
        return True
    if Solve(idx+1, sum):
        return True


for _ in range(testCase):
    N, K, nums = Input_Data()

    if Solve(0, 0):
        print("YES")
    else:
        print("NO")
