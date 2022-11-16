import sys

def Input_Data():
    readl = sys.stdin.readline
    K = int(readl())
    edges = [list(map(int,readl().split())) for _ in range(6)]
    return K, edges

sol = 0
K, edges = Input_Data()
edges = edges+edges[:3]

def Solve():
  global lastW,lastH,temp
  maxWidth = -1
  maxHeight = -1
  lastW = -1
  lastH = -1
  lastDir = -1
  temp = 0
  for dir,len in edges:
    if lastDir == 2 and dir == 4:
      temp = len*lastW
    if lastDir == 3 and dir ==2:
      temp = len*lastH
    if lastDir == 4 and dir == 1:
      temp = len*lastH
    if lastDir == 1 and dir ==3:
      temp = len*lastW
    if dir==1 or dir==2:
      maxWidth = max(maxWidth,len)
      lastW = len
    if dir==3 or dir==4:
      maxHeight = max(maxHeight,len)
      lastH = len
    lastDir = dir
  print((maxWidth*maxHeight-temp)*K)

Solve()