import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    return [['.']+list(readl().strip())+['.'] if 1<=r<=12 else ['.']*8 for r in range(14)]


readl = sys.stdin.readline
T = int(readl())

def Check():
  cnt = 0
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  visit = [[0]*8 for _ in range(14)]
  for i in range(1,13):
    for j in range(1,7):
      if map_puyo[i][j]==".":
        continue
      if visit[i][j]:
        continue
      curColor = map_puyo[i][j]
      curCnt = 1
      q = deque()
      q.append((i,j))
      cArr = []
      cArr.append((i,j))
      visit[i][j]=1
      while q:
        curRow,curCol = q.popleft()
        for r_d,c_d in dir:
          nextRow,nextCol = curRow+r_d,curCol+c_d
          if map_puyo[nextRow][nextCol]!=curColor:
            continue
          if visit[nextRow][nextCol]:
            continue
          visit[nextRow][nextCol] = 1
          curCnt+=1
          q.append((nextRow,nextCol))
          cArr.append((nextRow,nextCol))
      if curCnt<4:
        continue
      for sr,sc in cArr:
        map_puyo[sr][sc] = "."
      cnt+=1
  return cnt


def Boom():
  for i in range(1,7):
    row,puyo = 12,-1
    while True:
      while row>=1 and map_puyo[row][i]!=".":
        row-=1
      if row==0:
        break
      if puyo==-1:
        puyo = row-1
      while puyo>=1 and map_puyo[puyo][i]==".":
        puyo-=1
      if puyo==0:break
      map_puyo[row][i] = map_puyo[puyo][i]
      map_puyo[puyo][i] = "."
      row-=1

for _ in range(T):
  map_puyo = input_data()
  check = [[0]*14 for _ in range(8)]
  combo = 0
  while True:
    if Check()==0:
      break
    Boom()
    combo+=1
  print(combo)