import sys
from collections import deque
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    cards = list(map(int, readl().split()))
    M = int(readl())
    findCards = list(map(int, readl().split()))
    return N, M, cards, findCards


N, M, cards, findCards = Input_Data()
ans = []


def Solve():
    cards.sort()
    for i in findCards:
        low = bisect.bisect_left(cards, i)
        high = bisect.bisect_right(cards, i)
        if low >= N or cards[low] != i:
            ans.append(0)
            continue
        ans.append(high-low)
    print(*ans)


Solve()
