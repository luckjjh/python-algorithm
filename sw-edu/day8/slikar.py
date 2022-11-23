import sys
from collections import deque
readl = sys.stdin.readline

def Input_Data():
    R, C = map(int,readl().split())
    map_forest = [list(map(str,list(readl().rstrip()))) for _ in range(R)]
    return R,C,map_forest



T = int(readl())
for _ in range(T):
    R, C, map_forest = Input_Data()
    startRow,startCol = 0,0
    endRow,endCol = 0,0
    q = deque()
    dir = ((-1,0),(1,0),(0,-1),(0,1))

    for i in range(R):
      for j in range(C):
        if map_forest[i][j]=="D":
          endRow,endCol = i,j
        if map_forest[i][j]=="S":
          startRow,startCol = i,j
        if map_forest[i][j]=="*":
          q.append((i,j))
    
    q.appendleft((startRow,startCol))
    visit = [[0]*C for _ in range(R)]
    check = False
    while q:
      curRow,curCol = q.popleft()
      if check:
        break
      for r_d,c_d in dir:
        nextRow,nextCol = curRow+r_d,curCol+c_d
        if nextRow<0 or nextCol<0:
          continue
        if nextRow>=R or nextCol>=C:
          continue
        if map_forest[curRow][curCol]=="*":
          if map_forest[nextRow][nextCol]=="." or map_forest[nextRow][nextCol]=="S":
            map_forest[nextRow][nextCol] = "*"
            q.append((nextRow,nextCol))
        elif map_forest[curRow][curCol]=="S":
          if map_forest[nextRow][nextCol]==".":
            map_forest[nextRow][nextCol]="S"
            visit[nextRow][nextCol] = visit[curRow][curCol]+1
            q.append((nextRow,nextCol))
          elif map_forest[nextRow][nextCol]=="D":
            check = True
            visit[nextRow][nextCol] = visit[curRow][curCol]+1
            break
    if visit[endRow][endCol]==0:
      print("KAKTUS")
    else:
      print(visit[endRow][endCol])