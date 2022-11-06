import sys

def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  aList = [map(int,readl().split()) for _ in range(N)]
  return N,aList

N,aList = Input_Data()
maps = [[0]*101 for _ in range(101)]


def Solve():
  for row,col in aList:
    for i in range(10):
      for j in range(10):
        maps[row+i][col+j] = 1
  cnt = 0
  for i in maps:
    for item in i:
      if item:
        cnt+=1

  print(cnt)

Solve()