import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    aMap = [list(map(str, list(readl().rstrip()))) for _ in range(R)]
    return R, C, aMap


R, C, aMap = Input_Data()


def Solve(row, col, cnt):
    global maxLen
    maxLen = max(maxLen, cnt)
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for r_d, c_d in dir:
        nextRow, nextCol = row+r_d, col+c_d
        if nextRow < 0 or nextCol < 0:
            continue
        if nextRow >= R or nextCol >= C:
            continue
        if aMap[nextRow][nextCol] in ans:
            continue
        ans.add(aMap[nextRow][nextCol])
        Solve(nextRow, nextCol, cnt+1)
        ans.remove(aMap[nextRow][nextCol])


maxLen = -1
ans = set()
ans.add(aMap[0][0])
Solve(0, 0, 1)
print(maxLen)
