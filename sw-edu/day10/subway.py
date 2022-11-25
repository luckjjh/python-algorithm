import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M, K = map(int,readl().split())
    info = [list(map(int,readl().split()))for _ in range(M)]
    return N, M, K, info

sol = -1
N, M, K, info = Input_Data()
maps = [[0]*(N+1) for _ in range(N+1)]
for s,e in info:
  maps[s][e] = 1
  maps[e][s] = 1

sizeArr = []

def BFS(dist):
  q = deque()
  q.append(dist)
  size = 1
  while q:
    curDist = q.popleft()
    for i in range(1,N+1):
      if maps[curDist][i]==1 and not visit[i]:
        visit[i] = 1
        q.append(i)
        size+=1
  sizeArr.append(size)

def Solve():
  global visit
  visit = [0]*(N+1)
  for i in range(1,N+1):
    if not visit[i]:
      visit[i] = 1
      BFS(i)
  
  sizeArr.sort(reverse=True)
  sumSize = 0
  if len(sizeArr)<K+1:
    print(sum(sizeArr))
    return
  for i in range(K+1):
    sumSize+=sizeArr[i]
  print(sumSize)
Solve()
