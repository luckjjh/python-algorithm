import sys
from collections import deque

# 1 push
# 0 pop
# 2 len


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    cList = [list(map(int, readl().split())) for _ in range(N)]
    return N, cList


N, cList = Input_Data()


def Solve():
    q = deque()
    for i in range(N):
        if cList[i][0] == 0:
            if len(q):
                print(q.pop())
            else:
                print("E")
        elif cList[i][0] == 1:
            q.append(cList[i][1])
        elif cList[i][0] == 2:
            print(len(q))


Solve()
