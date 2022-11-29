import sys
from itertools import permutations

def input_data():
    readl = sys.stdin.readline
    B, N = map(int, readl().split())
    weight_ship = [int(readl()) for _ in range(B)]
    weight_passenger = [int(readl()) for _ in range(N)]
    return B, N, weight_ship, weight_passenger


maxW = -1

B, N, weight_ship, weight_passenger = input_data()
# 배 수, 승객 수, 각 배 최대 수용 무게, 각 승객 무게

def DFS(slevel,plevel):
  global maxW
  if plevel>=N:
    if slevel<B-1:
      maxW = max(maxW,sum(origin[slevel+1:B]))
    return
  if slevel>=B:
    return

  if origin[slevel]-weight_passenger[plevel]>=0:
    origin[slevel] = origin[slevel]-weight_passenger[plevel]
    DFS(slevel,plevel+1)
    origin[slevel] = origin[slevel]+weight_passenger[plevel]
  else:
    DFS(slevel+1,plevel)

def Solve():
  global origin
  if sum(weight_passenger)>sum(weight_ship):
    print(-1)
    return
  shipPerm = list(map(list,permutations(weight_ship,len(weight_ship))))
  for i in shipPerm:
    origin = i.copy()
    DFS(0,0)
  
  print(maxW)


Solve()