import sys
from itertools import combinations,permutations


def Input_Data():
    N, B = map(int, readl().split())
    height = [int(readl()) for _ in range(N)]
    return N, B, height


readl = sys.stdin.readline

curMin = 987654321

def Solve(idx, cur):
  global curMin
  if cur>=B:
    curMin = min(curMin,cur)
  if cur>=curMin:
    return
  for i in range(idx,len(height)):
    cur+=height[i]
    Solve(i+1,cur)
    cur-=height[i]

T = int(readl())
for _ in range(T):
    N, B, height = Input_Data()
    curMin = 987654321
    Solve(0,0)
    print(curMin-B)