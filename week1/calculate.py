import sys
from collections import deque

# zip 함수, stack 활용 사칙연산 로직 정리 필요


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int, str_exp[0::2]))
    ops = str_exp[1::2]
    return N, nums, ops


N, nums, ops = Input_Data()


def Solve():
    stack = deque()
    stack.append(nums[0])
    for op, num in zip(ops, nums[1:]):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            temp = stack.pop()
            stack.append(temp*num)
        elif op == '/':
            temp = stack.pop()
            if temp < 0:
                temp = -temp
                stack.append(-(temp//num))
            else:
                stack.append(temp//num)
    return sum(stack)


print(Solve())
