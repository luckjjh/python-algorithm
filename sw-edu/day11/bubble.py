import sys


def input_data():
  A, N = map(int, readl().split())
  W = list(map(int, readl().split()))
  return A, N, W


readl = sys.stdin.readline

minCnt = 987654321

def Solve(level,curSize,cnt):
  global minCnt
  if level==N:
    minCnt = min(minCnt,cnt)
    return
  if minCnt<=cnt:
    return
  
  if curSize>W[level]:
    Solve(level+1,curSize+W[level],cnt)
  else:
    if curSize!=0:
      Solve(level+1,curSize+curSize-1,cnt+1)
    Solve(level+1,curSize,cnt+1)



T = int(readl())
for t in range(1, T+1):
  minCnt = 987654321
  A, N, W = input_data()
  W.sort()
  Solve(0,A,0)
  print(f"Case #{t}:",minCnt)