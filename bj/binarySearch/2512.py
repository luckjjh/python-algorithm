import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    bList = list(map(int, readl().split()))
    budget = int(readl())
    return N, bList, budget


N, bList, budget = Input_Data()

maxBudget = max(bList)
minBudget = 1


def Solve():
    global maxBudget, minBudget
    if sum(bList) <= budget:
        print(maxBudget)
        return
    else:
        while minBudget <= maxBudget:
            mid = (maxBudget+minBudget)//2
            curSum = 0
            for i in bList:
                if mid >= i:
                    curSum += i
                else:
                    curSum += mid
            if curSum > budget:
                maxBudget = mid-1
            else:
                minBudget = mid+1
        print(maxBudget)


Solve()
