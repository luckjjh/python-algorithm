from re import I
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    sMap = [list(map(int, readl().split())) for _ in range(9)]
    return sMap


sMap = Input_Data()
zeroList = []
zeroCnt = 0
for i in range(9):
    for j in range(9):
        if sMap[i][j] == 0:
            zeroCnt += 1
            zeroList.append([i, j])
checkList = [0]*len(zeroList)


def CheckCol(col, n):
    for i in range(9):
        if n == sMap[i][col]:
            return False
    return True


def CheckRow(row, n):
    for i in range(9):
        if n == sMap[row][i]:
            return False
    return True


def CheckRect(row, col, n):
    nr = row//3*3
    nc = col//3*3
    for i in range(3):
        for j in range(3):
            if n == sMap[nr+i][nc+j]:
                return False
    return True


def Solve(level):
    if level == len(zeroList):
        for i in sMap:
            print(*i)
        exit(0)

    else:
        for j in range(1, 10):
            curRow, curCol = zeroList[level][0], zeroList[level][1]
            if CheckRow(curRow, j) and CheckCol(curCol, j) and CheckRect(curRow, curCol, j):
                sMap[curRow][curCol] = j
                Solve(level+1)
                sMap[curRow][curCol] = 0


Solve(0)
