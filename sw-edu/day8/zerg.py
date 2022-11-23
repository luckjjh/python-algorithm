import sys
from collections import deque
def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int, readl().split())
    map_zergling = [[0]+list(map(int, readl()[:-1]))+[0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    sc, sr = map(int, readl().split())
    return C, R, sc, sr, map_zergling


sol_time, sol_zergling = -1,-1


C, R, sc, sr, map_zergling = Input_Data()
remain = 0
for i in range(R+2):
  for j in range(C+2):
    if map_zergling[i][j]==1:
      remain+=1
def Solve():
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  startRow,startCol = sr,sc
  q = deque()
  q.append((startRow,startCol,0))
  map_zergling[startRow][startCol] = 0
  cnt = 1
  while q:
    curRow,curCol,curTime = q.popleft()
    for r_d,c_d in dir:
      nextRow,nextCol = curRow+r_d, curCol+c_d
      if nextRow<0 or nextCol<0:
        continue
      if nextRow>=R+2 or nextCol>=C+2:
        continue
      if map_zergling[nextRow][nextCol]==1:
        map_zergling[nextRow][nextCol] = 0
        q.append((nextRow,nextCol,curTime+1))
        cnt+=1
  print(curTime+3)
  print(remain-cnt)
Solve()