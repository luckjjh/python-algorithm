import sys
from collections import deque
import math

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_field = [[0] + list(map(int, readl().split()))  + [0] if 1<=r<=N else [0] * (N+2)  for r in range(N+2)]
	return N, map_field


sol = -1000000
N, map_field = Input_Data()
maxF = math.ceil((N*N)/2)

def BFS(r,c,cost):
  q = deque()
  q.append((r,c))
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  cnt = 1
  visit[r][c] = 1
  while q:
    if cnt==maxF:
      break
    curRow,curCol = q.popleft()
    for r_d, c_d in dir:
      nextRow,nextCol = curRow+r_d,curCol+c_d
      if nextRow<1 or nextCol<1:
        continue
      if nextRow>N or nextCol>N:
        continue
      if visit[nextRow][nextCol]:
        continue
      if abs(map_field[nextRow][nextCol]-map_field[curRow][curCol])<=cost:
        visit[nextRow][nextCol] = 1
        q.append((nextRow,nextCol))
        cnt+=1
  return cnt
def Solve():
  global visit,ans
  minH = sys.maxsize
  maxH = -1
  for i in range(1,N+1):
    for j in range(1,N+1):
      maxH = max(maxH,map_field[i][j])
      minH = min(minH,map_field[i][j])
  if minH==maxH:
    print(0)
    return

  high = maxH-minH
  low = 0
  while low<=high:
    curCnt = -1
    curCost = (low+high)//2
    visit = [[0]*(N+2) for _ in range(N+2)]
    for j in range(1,N+1):
      for k in range(1,N+1):
        if not visit[j][k]:
          temp = BFS(j,k,curCost)
          curCnt = max(curCnt,temp)
    if curCnt>=maxF:
      high = curCost-1
      ans = curCost
    else:
      low = curCost+1
  print(ans)
Solve()