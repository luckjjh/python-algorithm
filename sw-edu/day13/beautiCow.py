import sys
from collections import deque
from itertools import permutations,combinations

def Input_Data():
  readl = sys.stdin.readline
  N,M = map(int,readl().split())
  cowMap = [list(map(str,list(readl().rstrip()))) for _ in range(N)]
  return N,M,cowMap

N,M,cowMap = Input_Data()
axisArr = []

def Check():
  global visit
  visit = [[0]*M for _ in range(N)]
  curCnt = 0
  for i in range(N):
    for j in range(M):
      if cowMap[i][j]=="X" and not visit[i][j]:
        if curCnt==1:
          return False
        visit[i][j] = 1
        BFS(i,j)
        curCnt+=1
  return True

def BFS(r,c):
  q = deque()
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  q.append((r,c))
  while q:
    cr,cc = q.popleft()
    for rd,cd in dir:
      nr,nc = cr+rd,cc+cd
      if nr<0 or nc<0:
        continue
      if nr>=N or nc>=M:
        continue
      if cowMap[nr][nc]==".":
        continue
      if visit[nr][nc]:
        continue
      visit[nr][nc]=1
      q.append((nr,nc))
      
def Solve():
  for i in range(N):
    for j in range(M):
      if cowMap[i][j]==".":
        axisArr.append((i,j))

  for i in range(1,len(axisArr)+1):
    for j in list(combinations(axisArr,i)):
      for r,c in j:
        cowMap[r][c]="X"
      if Check():
        print(i)
        return
      for r,c in j:
        cowMap[r][c]="."

Solve()