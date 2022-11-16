import sys 
from collections import deque
def Input_Data():
    readl = sys.stdin.readline 
    N = int(readl()) 
    info = [list(map(int, readl().split())) for _ in range(N)] 
    return N, info 

maps = [[0]*102 for _ in range(102)]

# 입력받는 부분 
N, info = Input_Data() 
for row,col in info:
  for i in range(10):
    for j in range(10):
      maps[row+i][col+j] = 1
      
def Solve(row,col):

  cnt = 0
  q = deque()
  q.append((row,col))
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  while q:
    curRow,curCol = q.popleft()
    for r_d,c_d in dir:
      nextRow,nextCol = curRow+r_d,curCol+c_d
      if nextRow<0 or nextCol<0:
        continue
      if nextRow>=102 or nextCol>=102:
        continue
      if maps[nextRow][nextCol]==1:
        cnt+=1
      if maps[nextRow][nextCol]==0:
        maps[nextRow][nextCol]=2
        q.append((nextRow,nextCol))
  return cnt

ans = 0
for i in range(102):
  for j in range(102):
    if maps[i][j]==0:
      maps[i][j]=2
      temp = Solve(i,j)
      ans+=temp
print(ans)