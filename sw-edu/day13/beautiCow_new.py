import sys
from collections import deque
from itertools import permutations,combinations

def Input_Data():
  readl = sys.stdin.readline
  N,M = map(int,readl().split())
  cowMap = [list(map(str,list(readl().rstrip()))) for _ in range(N)]
  return N,M,cowMap

N,M,cowMap = Input_Data()
visit = [[0]*50 for _ in range(50)]
visit2 = [[[0]*50 for _ in range(50)] for _ in range(4)]
cnt = 1
dir = ((-1,0),(1,0),(0,-1),(0,1))
minCnt = sys.maxsize
q = deque()

def BFS(i):
  global minCnt
  dist = 0
  temp = [0]*4
  while q:
    curR,curC = q.popleft()
    for rd,cd in dir:
      nr,nc=curR+rd,curC+cd
      if nr<0 or nc<0:
        continue
      if nr>=N or nc>=M:
        continue
      if visit[nr][nc]!=i and not visit2[i][nr][nc]:
        visit2[i][nr][nc] = visit2[i][curR][curC]+1
        if visit[nr][nc]:
          if not temp[visit[nr][nc]]:
            temp[visit[nr][nc]]=1
            dist+=visit2[i][nr][nc]
        q.append((nr,nc))
  dist-=2
  minCnt = min(minCnt,dist)

def DFS(r,c):
  visit[r][c]=cnt
  for rd,cd in dir:
    nr,nc = r+rd,c+cd
    if nr<0 or nc<0:
      continue
    if nr>=N or nc>=M:
      continue
    if not visit[nr][nc] and cowMap[nr][nc]=="X":
      DFS(nr,nc)




for i in range(N):
  for j in range(M):
    if not visit[i][j] and cowMap[i][j]=='X':
      DFS(i,j)
      cnt+=1

for i in range(1,4):
  for j in range(N):
    for k in range(M):
      if visit[j][k]==i:
        q.append((j,k))
  BFS(i)

for i in range(N):
  for j in range(M):
    dist = 0
    for k in range(1,4):
      dist+=visit2[k][i][j]
    dist-=2
    minCnt = min(dist,minCnt)
print(minCnt)