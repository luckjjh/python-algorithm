import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int,readl().split())
    names = [readl().strip() for _ in range(N)]
    return N, K, names

sol = -1

N, K, names = Input_Data()
cntDict = dict()
nameLen = []
for i in names:
  nameLen.append(len(i))
for i in range(len(nameLen)):
  cntDict[nameLen[i]] = 0

def Solve():
  q = deque()
  cnt = 0
  for name in nameLen:
    if len(q)>K:
      temp = q.popleft()
      cntDict[temp]-=1
    q.append(name)
    cntDict[name]+=1
    if cntDict[name]>1:
      cnt+=cntDict[name]-1
  print(cnt)
Solve()