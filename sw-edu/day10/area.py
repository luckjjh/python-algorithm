import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C, K = map(int, readl().split())
    rects = [list(map(int,readl().split())) for _ in range(K)]
    return R, C, K, rects



R, C, K, rects = input_data()

def BFS(row,col):
  q = deque()
  q.append((row,col))
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  cnt = 1
  maps[row][col] = -1
  while q:
    curRow,curCol = q.popleft()
    for r_d,c_d in dir:
      nextRow,nextCol = curRow+r_d,curCol+c_d
      if nextRow<0 or nextCol<0:
        continue
      if nextRow>=C or nextCol>=R:
        continue
      if maps[nextRow][nextCol]==1:
        continue
      if maps[nextRow][nextCol]==-1:
        continue
      maps[nextRow][nextCol] = -1
      cnt+=1
      q.append((nextRow,nextCol))
  return cnt

def Solve():
  global maps
  maps = [[0]*(R) for _ in range(C)]
  for sr,sc,er,ec in rects:
    for i in range(sr,er):
      for j in range(sc,ec):
        maps[i][j]=1
  cntArr = []
  total = 0
  for i in range(C):
    for j in range(R):
      if maps[i][j]==0:
        curCnt = BFS(i,j)
        cntArr.append(curCnt)
        total+=1
  print(total)
  cntArr.sort()
  print(*cntArr)


Solve()