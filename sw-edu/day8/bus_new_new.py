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

bus = [0]*(K+1)
visit = [0]*(K+1)

for id,x1,y1,x2,y2 in list_bus:
  if x1>x2:
    x1,x2=x2,x1
  if y1>y2:
    y1,y2=y2,y1
  
  bus[id] = (x1,y1,x2,y2)

def Solve():
  q = deque()
  ans = 0
  for i in range(1,K+1):
    if bus[i][0]<=sx<=bus[i][2] and bus[i][1]<=sy<=bus[i][3]:
      q.append(i)
      visit[i] = 1
  while q:
    curBus = q.popleft()
    if bus[curBus][0]<=dx<=bus[curBus][2] and bus[curBus][1]<=dy<=bus[curBus][3]:
      ans = visit[curBus]
      break
    for nextBus in range(1,K+1):
      if not visit[nextBus]:
        if bus[curBus][0]<=bus[nextBus][2] and bus[nextBus][0]<=bus[curBus][2] \
          and bus[curBus][1]<=bus[nextBus][3] and bus[nextBus][1]<=bus[curBus][3]:
          visit[nextBus] = visit[curBus]+1
          q.append(nextBus)
  print(ans)

Solve()