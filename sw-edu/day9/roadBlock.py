import sys
import heapq

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    edges = [list(map(int, readl().split())) for _ in range(M)]
    return N, M, edges
    
sol = -1

N, M, edges = Input_Data()
curMax = 0

maps = [[0]*(N+1) for _ in range(N+1)]
for s,e,c in edges:
  maps[s][e] = c
  maps[e][s] = c
record = [0]*(N+1)

def Solve():
  global curMax
  pq = []
  dist = [sys.maxsize]*(N+1)
  heapq.heappush(pq,(0,1))
  dist[1] = 0
  while pq:
    curCost,curDist = heapq.heappop(pq)
    for i in range(1,N+1):
      if maps[curDist][i]>0 and maps[curDist][i]+curCost<dist[i]:
        dist[i] = maps[curDist][i]+curCost
        record[i] = curDist
        heapq.heappush(pq,((maps[curDist][i]+curCost),i))
  curMax = max(curMax,dist[N])


def Run():
  Solve()
  temp = []
  idx = N
  while idx!=0:
    temp.append(idx)
    idx = record[idx]
  temp.reverse()
  firstMin = curMax
  for i in range(len(temp)-1):
    maps[temp[i]][temp[i+1]] = maps[temp[i]][temp[i+1]]*2
    maps[temp[i+1]][temp[i]] = maps[temp[i+1]][temp[i]]*2
    Solve()
    maps[temp[i]][temp[i+1]] = maps[temp[i]][temp[i+1]]/2
    maps[temp[i+1]][temp[i]] = maps[temp[i+1]][temp[i]]/2
  print(int(curMax-firstMin))

Run()