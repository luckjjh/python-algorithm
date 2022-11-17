import sys

def Input_Data():
    readl = sys.stdin.readline
    N, C = map(int,readl().split())
    M = int(readl())
    info = [list(map(int,readl().split())) for _ in range(M)]
    return N, C, M, info    

sol = 0

N, C, M, info = Input_Data()
# N 마을 개수
# C 트럭 용량
# M 박스 정보 개수
# info start, end, 개수

info.sort(key = lambda i:(i[1]))

def Solve():
  cost = 0
  truck = [C]*(N+1)
  for i in range(len(info)):
    curCost = C
    for j in range(info[i][0],info[i][1]):
      curCost = min(curCost,truck[j])
    curCost = min(curCost,info[i][2])
    for j in range(info[i][0],info[i][1]):
      truck[j] -= curCost
    cost +=curCost
  print(cost)
Solve()