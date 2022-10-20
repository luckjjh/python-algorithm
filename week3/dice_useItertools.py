import sys
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M


N, M = Input_Data()

dice = [i for i in range(1, 7)]


def Solve():
    if M == 1:
        arr = list(product(dice, repeat=N))
    elif M == 2:
        arr = list(combinations_with_replacement(dice, N))
    elif M == 3:
        arr = list(permutations(dice, N))
    for i in range(len(arr)):
        for j in arr[i]:
            print(j, end=' ')
        print()


Solve()
