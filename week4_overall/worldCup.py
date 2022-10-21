import sys
from itertools import combinations


def Input_Data():
    readl = sys.stdin.readline
    table = [[0]*3 for _ in range(6)]
    temp = list(map(int, readl().split()))
    idx = 0
    for i in range(6):
        for j in range(3):
            table[i][j] = temp[idx]
            idx += 1
    return table


def Solve(round):
    global check
    if round == 15:
        for i in table:
            if sum(i) != 0:
                return
        check = True
        return
    t1, t2 = match[round]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if table[t1][x] > 0 and table[t2][y] > 0:
            table[t1][x] -= 1
            table[t2][y] -= 1
            Solve(round+1)
            table[t1][x] += 1
            table[t2][y] += 1


match = list(combinations(range(6), 2))
ans = [0]*4

for i in range(4):
    table = Input_Data()
    check = False
    Solve(0)
    if check:
        ans[i] = 1


print(*ans)
