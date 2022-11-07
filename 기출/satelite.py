import sys
from collections import deque

def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  maps = [list(map(int,list(readl().rstrip()))) for _ in range(N)]
  return N,maps

N,maps = Input_Data()

def Solve(row,col):
  q = deque()
  q.append((row,col,1))
  visit[row][col] = 1
  dir = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
  while q:
    curRow,curCol,curSize = q.popleft()
    for r_d, c_d in dir:
      nextRow,nextCol = curRow+r_d, curCol+c_d
      if nextRow<0 or nextCol<0:
        continue
      if nextRow>=N or nextCol>=N:
        continue
      if visit[nextRow][nextCol]:
        continue
      visit[nextRow][nextCol] = 1
      if maps[nextRow][nextCol]==0:
        continue
      q.append((nextRow,nextCol,curSize+1))
  return curSize


def Run():
  maxSize = -1
  global visit
  visit = [[0]*N for _ in range(N+1)]
  for i in range(N):
    for j in range(N):
      if maps[i][j] and not visit[i][j]:
        maxSize = max(maxSize,Solve(i,j))
  print(maxSize)

Run()