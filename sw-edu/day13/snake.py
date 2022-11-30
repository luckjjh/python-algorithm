import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    K = int(readl())
    pos = [tuple(map(int, readl().split())) for _ in range(K)]
    L = int(readl())
    cmd_list = [list(readl().split()) for _ in range(L)]

    return N, K, pos, L, cmd_list

sol = -1

N, K, pos, L, cmd_list = input_data()
# 격자 크기, 과일 개수, 과일 정보, 이동 경로 개수, 이동 경로(x초 이후에 L 왼쪽 D 오른쪽)


def Solve():
  gameMap = [[0]*N for _ in range(N)]
  for r,c in pos:
    gameMap[r-1][c-1] = -1
  gameMap[0][0] = 1
  dir = ((0,1),(1,0),(0,-1),(-1,0))#우 하 좌 상
  q = deque()
  for time,d in cmd_list:
    q.append((time,d))
  curDir = 0
  headRow,headCol = 0,0
  tailRow,tailCol = 0,0
  stime = 0
  check = True
  while True:
    if q:
      curTime,dirCmd = q.popleft()
      iter = int(curTime)-stime
    else:
      iter=N
    for _ in range(iter):
      stime+=1
      step = dir[curDir]
      headRow+=step[0]
      headCol+=step[1]
      if headRow<0 or headCol<0:
        # 벽
        check = False
        break
      if headRow>=N or headCol>=N:
        # 벽
        check = False
        break
      if gameMap[headRow][headCol]>0:
        # 자기자신
        check = False
        break
      if gameMap[headRow][headCol]==-1:
        # 사과인 경우
        gameMap[headRow][headCol]=stime+1
        # 몸 늘리고 끝
      if gameMap[headRow][headCol]==0:
        # 빈공간 인경우
        gameMap[headRow][headCol] = stime+1
        for r,c in dir:
          nextRow,nextCol = tailRow+r,tailCol+c
          if nextRow<0 or nextCol<0:
            continue
          if nextRow>=N or nextCol>=N:
            continue
          if gameMap[tailRow][tailCol]+1==gameMap[nextRow][nextCol]:
            gameMap[tailRow][tailCol] = 0
            tailRow=nextRow
            tailCol=nextCol
            break
        
        # 꼬리 줄이고 몸 늘리고 끝
    if dirCmd=="L":
      if curDir-1==-1:
        curDir = 3
      else:
        curDir-=1
    elif dirCmd=="D":
      if curDir+1==4:
        curDir = 0
      else:
        curDir+=1
    if not check:
      break
    
  print(stime)

Solve()
