import sys
from itertools import permutations

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    relation = [list(map(int, readl().split())) for i in range(M)]    
    bonus = list(map(int, readl().split()))
    return N, M, relation, bonus



N, M, relation, bonus = input_data()

rDcit = dict()
for i in range(1,N+1):
  rDcit[i] = []
for u,d in relation:
  rDcit[u].append(d)


def Solve():
  for per in list(permutations(bonus,len(bonus))):
    for i in range(len(per)):
      check = True
      for j in rDcit[i+1]:
        if per[i]<=per[j-1]:
          check = False
          break
      if check:
        print(*per)
        return
      else:
        break

Solve()