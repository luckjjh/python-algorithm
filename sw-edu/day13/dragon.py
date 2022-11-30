import sys
from collections import deque
def input_data():
    L, R, C = map(int, readl().split())
    map_dungeon = [[list(readl().strip())for r in range(R+1)] for l in range(L)]
    return L, R, C, map_dungeon


readl = sys.stdin.readline
def Solve():
  visit = [[[0]*C for _ in range(R)] for _ in range(L)]
  dir = ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0))
  q = deque()
  q.append((startD,startR,startC,0))
  visit[startD][startR][startC] = 1
  while q:
    curD,curR,curC,curTime = q.popleft()
    if curD==endD and curR==endR and curC==endC:
      return curTime
    for dd,rd,cd in dir:
      nextD,nextR,nextC = curD+dd,curR+rd,curC+cd
      if nextD<0 or nextR<0 or nextC<0:
        continue
      if nextD>=L or nextR>=R or nextC>=C:
        continue
      if map_dungeon[nextD][nextR][nextC]=='#':
        continue
      if visit[nextD][nextR][nextC]:
        continue
      visit[nextD][nextR][nextC] = 1
      q.append((nextD,nextR,nextC,curTime+1))
  return -1

while 1:
    L, R, C, map_dungeon = input_data()
    if L == 0 and R == 0 and C == 0: break
    for i in range(L):
      for j in range(R):
        for k in range(C):
          if map_dungeon[i][j][k]=="S":
            startD,startR,startC = i,j,k
          if map_dungeon[i][j][k]=="E":
            endD,endR,endC = i,j,k
    ans = Solve()
    if ans==-1:
      print("Trapped!")
    else:
      print(f"Escaped in {ans} minute(s).")