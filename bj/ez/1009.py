import sys


def Input_Data():
    readl = sys.stdin.readline
    a, b = map(int, readl().split())
    return a, b


def Solve():
    num = pow(a, b, 10)
    if num:
        print(num)
    else:
        print(10)


tc = int(sys.stdin.readline())
for _ in range(tc):
    a, b = Input_Data()
    Solve()
