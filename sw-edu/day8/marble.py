import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int,readl().split())
	map_game = [readl().strip() for _ in range(R)]
	return R, C, map_game


sol = []
T = int(input())
for t in range(T):
  R, C, map_game = Input_Data()
  redRow,redCol,blueRow,blueCol,endRow,endCol=0,0,0,0,0,0
  map_game = [[0]*C for _ in range(R)]

  for i in range(R):
    for j in range(C):
      if map_game[i][j]=="R":
        redRow = i
        redCol = j
      if map_game[i][j]=="B":
        blueRow = i
        blueCol = j
  q = deque()
  q.append((redRow,redCol,blueRow,blueCol,0))
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  curMin = 987654321
  chk = [[[[0] * C for _ in range(R)] for _ in range(C)] for _ in range(R)]
  chk[redRow][redCol][blueRow][blueCol] = 1
  while q:
    curRrow,curRcol,curBrow,curBcol,curCnt = q.popleft()
    if curCnt==10:
      break
    for r_d,c_d in dir:
      nextRrow,nextRcol,nextBrow,nextBcol = curRrow+r_d,curRcol+c_d,curBrow+r_d,curBcol+c_d
      if map_game[nextBrow][nextBcol]=="#":
        nextBrow,nextBcol = curBrow,curBcol
      if map_game[nextBrow][nextBcol]=="H":
        continue

      if map_game[nextRrow][nextRcol]=="#":
        nextRrow,nextRcol = curRrow,curRcol
      if map_game[nextRrow][nextRcol]=="H":
        curMin = min(curMin,curCnt+1)
      if nextBrow==nextRrow and nextBcol==nextRcol:
        continue
      if chk[nextRrow][nextRcol][nextBrow][nextBcol]:
        continue
      chk[nextRrow][nextRcol][nextBrow][nextBcol] = 1
      q.append((nextRrow,nextRcol,nextBrow,nextBcol,curCnt+1))
  sol.append(curMin)

print(*sol, sep='\n')