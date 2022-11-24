import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_sand = [['.'] + list(readl()[:-1]) + ['.'] if 1<=r<=R else ['.'] * (C+2) for r in range(R+2)]
    return R, C, map_sand

sol = -1
R, C, map_sand = input_data()
cCnt = 0


def Solve():
  global cCnt,lastCnt
  visit = [[0]*(C+2) for _ in range(R+2)]
  q = deque()
  for i in range(R+2):
    for j in range(C+2):
      if not map_sand[i][j].isdigit():
        q.append((i,j))
        map_sand[i][j] = 0
      else:
        map_sand[i][j] = int(map_sand[i][j])
  dir = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
  while q:
    curRow,curCol = q.popleft()
    for r_d,c_d in dir:
      nextRow,nextCol = curRow+r_d,curCol+c_d
      if nextRow<0 or nextCol<0:
        continue
      if nextRow>R+1 or nextCol>C+1:
        continue
      if map_sand[nextRow][nextCol]>0:
        temp = map_sand[nextRow][nextCol]-1
        map_sand[nextRow][nextCol] = temp
        if map_sand[nextRow][nextCol]==0:
          visit[nextRow][nextCol]=visit[curRow][curCol]+1
          cCnt = max(cCnt,visit[nextRow][nextCol])
          q.append((nextRow,nextCol))
  print(cCnt)


Solve()
