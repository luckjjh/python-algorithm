import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    homeRow, homeCol = map(int, readl().split())
    cAxis = [list(map(int, readl().split())) for _ in range(N)]
    festRow, festCol = map(int, readl().split())
    return N, homeRow, homeCol, cAxis, festRow, festCol


N, homeRow, homeCol, cAxis, festRow, festCol = Input_Data()


def Solve():
