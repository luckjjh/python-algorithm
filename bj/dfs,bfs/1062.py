import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    words = list(str(readl().rstrip()) for _ in range(N))
    return N, K, words


N, K, words = Input_Data()

charSet = set()

for i in words:
    for j in i:
        charSet.add(j)

antatica = ['a', 'n', 't', 'i', 'c']
ans = []
maxCnt = 0
K -= len(antatica)
for item in antatica:
    charSet.remove(item)

chatList = list(charSet)


def CountWords():
    cnt = 0
    for word in words:
        check = True
        for chr in word[4:-4]:
            if chr in ans or chr in antatica:
                check = True
            else:
                check = False
                break
        if check:
            cnt += 1
    return cnt


def Solve(idx, n):
    global maxCnt
    if n == K:
        maxCnt = max(CountWords(), maxCnt)
        return
    else:
        for i in range(idx, len(chatList)):
            ans.append(chatList[i])
            Solve(i+1, n+1)
            ans.pop()


if K >= len(chatList):
    print(N)
elif K >= 0:
    Solve(0, 0)
    print(maxCnt)
else:
    print(0)
