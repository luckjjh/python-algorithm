import sys
from collections import deque


def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  startRow,startCol = map(int,readl().split())
  cList = [list(map(int,readl().split())) for _ in range(N)]
  endRow,endCol = map(int,readl().split())
  return N,startRow,startCol,cList,endRow,endCol


def Solve():
  q = deque()
  q.append((startRow,startCol))
  while q:
    curRow,curCol = q.popleft()
    if abs(curRow-endRow)+abs(curCol-endCol)<=1000:
      print('happy')
      return
    else:
      for i in range(len(cList)):
        next = cList[i]
        if not visit[i]:
          if abs(next[0]-curRow)+abs(next[1]-curCol)<=1000:
            q.append((next[0],next[1]))
            visit[i] = 1
  print('sad')

tc = int(sys.stdin.readline())

for _ in range(tc):
  N,startRow,startCol,cList,endRow,endCol = Input_Data()
  visit = [0]*N
  Solve()
