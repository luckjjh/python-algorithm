from curses.ascii import isalpha
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    cList = list(map(str, list(readl().rstrip())))
    return cList


cList = Input_Data()


def Solve():
    oper = deque()
    nums = deque()
    for i in cList:
        if i.isalpha():
            nums.append(i)
        else:
            if i == '(':
                oper.append(i)
            if i == ')':
                while oper[-1] != '(':
                    temp = oper.pop()
                    nums.append(temp)
                oper.pop()
            if i == '+' or i == '-':
                while oper and oper[-1] != '(':
                    temp = oper.pop()
                    nums.append(temp)
                oper.append(i)
            if i == '*' or i == '/':
                while oper and (oper[-1] == '*' or oper[-1] == '/'):
                    temp = oper.pop()
                    nums.append(temp)
                oper.append(i)
    while oper:
        nums.append(oper.pop())

    print(*nums, sep='')


Solve()
