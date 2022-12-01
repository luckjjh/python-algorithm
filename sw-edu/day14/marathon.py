import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [list(map(int,readl().split())) for _ in range(N)]
    return N, pos

N, pos = input_data()

def CalcDistance(s,e):
  return abs(s[0]-e[0])+abs(s[1]-e[1])

def Solve():
  distArr = []
  for i in range(len(pos)-1):
    distArr.append(CalcDistance(pos[i],pos[i+1]))
  tempArr = []
  for i in range(len(distArr)-1):
    tempArr.append(distArr[i]+distArr[i+1])
  diffArr = []
  for i in range(len(distArr)-1):
    diffArr.append(CalcDistance(pos[i],pos[i+2]))
  maxDiff = -1
  for i in range(len(tempArr)):
    if maxDiff<abs(tempArr[i]-diffArr[i]):
      maxDiff = abs(tempArr[i]-diffArr[i])
  print(sum(distArr)-maxDiff)

Solve()