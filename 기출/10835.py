import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    left = list(map(int, readl().split()))
    right = list(map(int, readl().split()))
    return N, left, right


N, left, right = Input_Data()


def Solve():
    dp = [[0]*N+1 for _ in range(N+1)]
    leftD = deque(left)
    rightD = deque(right)
