import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    return [['.']+list(readl().strip())+['.'] if 1<=r<=12 else ['.']*8 for r in range(14)]


readl = sys.stdin.readline
T = int(readl())


def Solve(r,c,color):
    dir = ((-1,0),(1,0),(0,-1),(0,1))
    q = deque()
    q.append((r,c))
    check[r][c] = 1
    cnt = 1
    while q:
      curRow,curCol = q.popleft()
      for r_d,c_d in dir:
        nextRow,nextCol = curRow+r_d, curCol+c_d
        if nextRow<0 or nextCol<0:
          continue
        if nextRow>=14 or nextCol>=8:
          continue
        if map_puyo[nextRow][nextCol]!=color:
          continue
        if check[nextRow][nextCol]:
          continue
        check[nextRow][nextCol] = 1
        cnt+=1
        q.append((nextRow,nextCol))
    if cnt>=4:
      return True
    else:
      return False

def Boom(r,c,color):
    q = deque()
    q.append((r,c))
    dir = ((-1,0),(1,0),(0,-1),(0,1))
    while q:
      curRow,curCol = q.popleft()
      for r_d,c_d in dir:
        nextRow,nextCol = curRow+r_d,curCol+c_d
        if nextRow<0 or nextCol<0:
          continue
        if nextRow>=14 or nextCol>=8:
          continue
        if map_puyo[nextRow][nextCol]!=color:
          continue
        map_puyo[nextRow][nextCol] = '.'
        q.append((nextRow,nextCol))
    
    for i in range(12,-1,-1):
      for j in range(8):
        if map_puyo[i][j].isalpha() and map_puyo[i+1][j]=='.':
          ands

for _ in range(T):
    map_puyo = input_data()
    check = [[0]*14 for _ in range(8)]
    for i in range(14):
      for j in range(8):
        if not check[i][j] and map_puyo[i][j].isalpha():
          if Solve(i,j,map_puyo[i][j]):
              Boom(i,j,map_puyo[i][j])
          
