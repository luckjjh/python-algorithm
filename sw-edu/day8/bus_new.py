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


def Solve():
  bus = [0]*(K+1)
  visit = [0]*(K+1)
  for id,x1,y1,x2,y2 in list_bus:
    if x1==x2:
      bus[id] = sorted([(x1,y1),(x2,y2)], key=lambda i:i[1])
    else:
      bus[id] = sorted([(x1,y1),(x2,y2)], key=lambda i:i[0])

  startArr=[]
  endArr=[]

  for i in range(1,K+1):
    startBus,endBus = bus[i][0],bus[i][1]

    if startBus[0]<=sx<=endBus[0] and startBus[1]<=sy<=endBus[1]:
      startArr.append(i)
      visit[i] = 1
    
    if startBus[0] <= dx <= endBus[0] and startBus[1]<=dy<=endBus[1]:
      endArr.append(i)

  q = deque()

  for id in startArr:
    q.append((id,1))
  
  while q:
    curBus,cnt = q.popleft()

    if curBus in endArr:
      print(cnt)
      break
  
    for i in range(1,K+1):
      if not visit[i]:
        if check(curBus,i,bus):
          visit[i] = 1
          q.append((i,cnt+1))


def check(curBus,goBus,bus):
  curBusS,curBusE = bus[curBus][0],bus[curBus][1]
  goBusS,goBusE = bus[goBus][0],bus[goBus][1]

  if curBusS[1]==curBusE[1] and goBusS[1]==goBusE[1]:
    if curBusS[1]==curBusE[1]==goBusS[1]==goBusE[1]:
      if curBusS[0]<=goBusS[0]<=curBusE[0] or curBusS[0]<=goBusE[0]<=curBusE[0]:
        return True
    return False
  
  elif curBusS[0]==curBusE[0] and goBusS[0]==goBusE[0]:
    if curBusS[0]==curBusE[0]==goBusS[0]==goBusE[0]:
      if curBusS[1]<=goBusS[1]<=curBusE[1] or curBusS[1]<=goBusE[1]<=curBusE[1]:
        return True
    return False
  
  else:
    if goBusS[1]==goBusE[1]:
      if curBusS[1]<=goBusS[1]<=curBusE[1]:
        if goBusS[0]<=curBusS[0]<=goBusE[0]:
          return True
      return False
    if goBusS[0]==goBusE[0]:
      if curBusS[0]<=goBusS[0]<=curBusE[0]:
        if goBusS[1]<=curBusS[1]<=goBusE[1]:
          return True
      return False
Solve()