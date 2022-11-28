import sys
from itertools import combinations

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight

sol = -1
N, weight = input_data()
maxCnt = -1
visit = [0]*N
weight.sort()

def Solve(level,curWeight,cnt):
  global maxCnt
  maxCnt = max(maxCnt,cnt)
  if level==N:
    return
  if cnt + N - level <= maxCnt:
    return
  curStr = list(str(curWeight))[::-1]
  nextStr = list(str(weight[level]))[::-1]
  minLen = min(len(curStr),len(nextStr))
  check = True
  for i in range(minLen):
    if int(curStr[i])+int(nextStr[i])>=10:
      check = False
      break
  if check:
    Solve(level+1,weight[level]+curWeight,cnt+1)
  Solve(level+1,curWeight,cnt)

Solve(0,0,0)
print(maxCnt)