import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    k = int(readl())
    return N, k


N, k = Input_Data()
ans = 0


def Solve():
    start, end = 1, k
    while start <= end:
        mid = (start+end)//2
        print(mid)
        temp = 0
        for i in range(1, N+1):
            temp += min(mid//i, N)
        if temp >= k:
            ans = mid
            end = mid-1
        else:
            start = mid + 1
    print(ans)


Solve()
