import sys
from collections import deque
import copy


def Input_Data():
    readl = sys.stdin.readline
    L = int(readl())
    N = int(readl())
    dist = [0] + list(map(int, readl().split()))
    time = [0] + list(map(int, readl().split())) + [0]
    return L, N, dist, time


L, N, dist, time = Input_Data()

curMin = sys.maxsize
curMinArr = []


def Solve():
  q = deque()
  check = [sys.maxsize]*(N+2)
  path = [0]*(N+2)
  q.append((0,0))
  check[0] = 0
  if sum(dist)<=L:
    print(0)
  while q:
    curDist,curTime = q.popleft()
    if check[curDist]<curTime:
      continue
    sumDist = 0
    for i in range(curDist+1,N+2):
      sumDist+=dist[i]
      if sumDist>L:break
      if check[i]<=curTime+time[i]:
        continue
      check[i] = curTime+time[i]
      path[i] = curDist
      q.append((i,curTime+time[i]))
  print(check[N+1])
  pos = path[N+1]
  route = []
  while pos!=0:
    route.append(str(pos))
    pos = path[pos]
  if len(route)>0:
    print(len(route))
    route.reverse()
    print(*route)
Solve()
