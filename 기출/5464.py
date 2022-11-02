import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    cost = [int(readl()) for _ in range(N)]
    cars = [int(readl()) for _ in range(M)]
    sequen = [int(readl()) for _ in range(M*2)]
    return N, M, cost, cars, sequen


N, M, cost, cars, sequen = Input_Data()


def Solve():
    q = deque()
    sumCost = 0
    parking = [0]*N
    for step in sequen:
        if q:
            for i in range(len(parking)):
                if parking[i] == 0:
                    temp = q.popleft()
                    parking[i] = temp
                    sumCost += cost[i]*cars[temp-1]

        if step > 0:
            check = True
            for i in range(len(parking)):
                if parking[i] == 0:
                    check = False
                    parking[i] = step
                    sumCost += cost[i]*cars[step-1]
                    break
            if check:
                q.append(step)
        elif step < 0:
            step = -step
            for i in range(len(parking)):
                if parking[i] == step:
                    parking[i] = 0

    print(sumCost)


Solve()
