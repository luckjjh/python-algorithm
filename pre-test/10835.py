import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    leftDeq = list(map(int, readl().split()))
    rightDeq = list(map(int, readl().split()))
    return N, leftDeq, rightDeq


N, leftDeq, rightDeq = Input_Data()


def Solve():
