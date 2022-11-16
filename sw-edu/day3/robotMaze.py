import sys
from collections import deque

def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  maps = [list(map(int,list(readl().rstrip()))) for _ in range(N)]
  dir = list(map(int,readl().split()))
  # 1 아래 2 왼쪽 3 위 4 오른쪽
  return N,maps,dir

N,maps,dir = Input_Data()

visit = [[0]*N for _ in range(N)]
dirArr = []
for i in dir:
  if i==1:
    dirArr.append((1,0))
  elif i==2:
    dirArr.append((0,-1))
  elif i==3:
    dirArr.append((-1,0))
  elif i==4:
    dirArr.append((0,1))

def Solve():
  curRow,curCol = 0,0
  curDir = 0
  cnt=0
  while True:
    nextRow,nextCol = curRow+dirArr[curDir][0],curCol+dirArr[curDir][1]
    if nextRow<0 or nextCol<0:
      curDir = (curDir+1)%4
      continue
    if nextRow>=N or nextCol>=N:
      curDir = (curDir+1)%4
      continue
    if maps[nextRow][nextCol]==1:
      curDir = (curDir+1)%4
      continue
    if visit[nextRow][nextCol]:
      break
    visit[nextRow][nextCol] = 1
    cnt+=1
    curRow=nextRow
    curCol=nextCol
  print(cnt)
Solve()