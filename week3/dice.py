from re import I
import sys
# 주사위를 던진 횟수 N과 출력형식 M을 입력 받아서 M의 값에 따라 각각 아래와 같이 출력하는 프로그램을 작성하시오.
# M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
# M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
# M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
# * 중복의 예
# 1 1 2 와 중복 : 1 2 1, 2 1 1
# 1 2 3 과 중복 : 1 3 2, 2 1 3, 2 3 1, 3 1 2


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M


N, M = Input_Data()
dice = [0]*N
useNum = [0]*7


def Dice1(level):
    if level == N:
        print(*dice)
        return
    for i in range(1, 7):
        dice[level] = i
        Dice1(level+1)


def Dice2(level, start):
    if level == N:
        print(*dice)
        return
    for i in range(start, 7):
        dice[level] = i
        Dice2(level+1, i)


def Dice3(level):
    if level == N:
        print(*dice)
        return
    for i in range(1, 7):
        if useNum[i] == 1:
            continue
        useNum[i] = 1
        dice[level] = i
        Dice3(level+1)
        useNum[i] = 0


def Solve():
    if M == 1:
        Dice1(0)
    elif M == 2:
        Dice2(0, 1)
    elif M == 3:
        Dice3(0)


Solve()
