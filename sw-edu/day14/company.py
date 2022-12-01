import sys


def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    relation = [list(map(int, readl().split())) for i in range(M)]    
    bonus = list(map(int, readl().split()))
    return N, M, relation, bonus



N, M, relation, bonus = input_data()

uDcit = dict()
dDcit = dict()

for i in range(1,N+1):
  dDcit[i] = []
for u,d in relation:
  dDcit[u].append(d)

for i in range(1,N+1):
  uDcit[i] = []
for u,d in relation:
  uDcit[d].append(u)


bonusCheck = [0]*(N+1)

def Check(level):
  for i in dDcit[level]:
    if ans[level]<=ans[i] and ans[i]!=0:
      return False
  for i in uDcit[level]:
    if ans[level]>=ans[i] and ans[i]!=0:
      return False
  return True


def DFS(level):
  if level==N+1:
    print(*ans[1:])
    exit(0)
  for i in range(len(bonus)):
    if bonusCheck[i]:
      continue
    bonusCheck[i] = 1
    ans[level] = bonus[i]
    if Check(level):
      DFS(level+1)
    bonusCheck[i] = 0
    ans[level] = 0

def Solve():
  global ans
  ans = [0]*(N+1)
  DFS(1)

Solve()