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
  head = [0,0]
  tail = [0,0]
  gameMap = [[0]*N for _ in range(N)]
  for r,c in pos:
    gameMap[r-1][c-1] = -1
  gameMap[0][0] = 1
  for i in gameMap:
      print(i)
  dir = ((0,1),(1,0),(0,-1),(-1,0))#우 하 좌 상
  q = deque()
  for time,d in cmd_list:
    q.append((time,d))
  curDir = 0
  stime = 0
  check = True
  while True:
    stime+=1
    if q[0][0]==stime:
      curTime,dirCmd = q.popleft()
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
    head[0]+=dir[curDir][0]
    head[1]+=dir[curDir][1]
    if head[0]<0 or head[1]<0:
      break
    if head[0]>=N or head[1]>=N:
      break
    if gameMap[head[0]][head[1]]>0:
      break
    if gameMap[head[0]][head[1]]==-1:
      gameMap[head[0]][head[1]] = stime+1
    if gameMap[head[0]][head[1]]==0:
      for r,c in dir:
        gameMap[head[0]][head[1]] = stime+1
        nexttr,nexttc = tail[0]+r,tail[1]+c
        if nexttr<0 or nexttc<0:
          continue
        if nexttr>=N or nexttc>=N:
          continue
        if gameMap[nexttr][nexttc]==gameMap[tail[0]][tail[1]]+1:
          gameMap[tail[0]][tail[1]]=0
          tail[0]=nexttr
          tail[1]=nexttc
          break
      
    for i in gameMap:
      print(i)

    print("_")
  print(stime)

Solve()