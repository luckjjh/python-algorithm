import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    M, N = map(int, readl().split())
    K = int(readl())
    list_bus = [list(map(int, readl().split())) for _ in range(K)]
    sx, sy, dx, dy = map(int, readl().split())
    return M, N, K, list_bus, sx, sy, dx, dy

M, N, K, list_bus, sx, sy, dx, dy = Input_Data()

horizonBus = [[] for _ in range(N+1)]
verticalBus = [[] for _ in range(M+1)]



for id,x1,y1,x2,y2 in list_bus:
  if x1==x2:
    if y1>y2:
      y1,y2 = y2,y1
    verticalBus[x1].append([id,y1,y2,sys.maxsize])
  else:
    if x1>x2:
      x1,x2 = x2,x1
    horizonBus[y1].append([id,x1,x2,sys.maxsize])



def Solve():
  q = deque()
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  q.append((sx,sx,sy,sy,0))
  ans = sys.maxsize
  while q:
    comeX,goX,comeY,goY,curDist = q.popleft()

    if comeX<=dx<=goX and comeY<=dy<=goY:
      ans = min(ans,curDist)

    for i in range(comeY,goY+1):
      for j in range(len(horizonBus[i])):
        temp,comeP,goP,nextDist = horizonBus[i][j]
        if (comeP<=comeX<=goP or comeP<=goX<=goP) and nextDist>curDist+1:
          horizonBus[i][j]=[temp,comeP,goP,curDist+1]
          q.append((comeP,goP,i,i,curDist+1))

    for i in range(comeX,goX+1):
      for j in range(len(verticalBus[i])):
        temp,comeP,goP,nextDist = verticalBus[i][j]
        if (comeP<=comeY<=goP or comeP<=goY<=goP) and nextDist>curDist+1:
          verticalBus[i][j]=[temp,comeP,goP,curDist+1]
          q.append((i,i,comeP,goP,curDist+1))
        
  print(ans)
Solve()