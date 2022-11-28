import sys
import copy


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    cost = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
    return N, cost



N, cost = Input_Data()

minCost = 987654321

def Solve(idx,curcost):
  global minCost,sol
  if idx>N:
    if minCost>curcost:
      minCost = curcost
      sol = copy.deepcopy(ans)
  if minCost<=curcost:
    return
  for i in range(1,N+1):
    if visit[i]:
      continue
    visit[i] = 1
    ans[idx] = i
    Solve(idx+1,curcost+cost[idx][i])
    ans[idx] = 0
    visit[i] = 0

ans = [0]*(N+1)
visit = [0]*(N+1)

Solve(1,0)
print(minCost)
print(*sol[1:])