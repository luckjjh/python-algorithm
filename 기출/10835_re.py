import sys

def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  left = list(map(int,readl().split()))
  right = list(map(int,readl().split()))
  return N,left,right


N,left,right = Input_Data()
dp = [[0]*(N+1) for _ in range(N+1)]
def Solve():
  for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
      if right[j]<left[i]:
        dp[i][j] = max(dp[i][j+1]+right[j],dp[i+1][j],dp[i+1][j+1])
      else:
        dp[i][j] = max(dp[i+1][j],dp[i+1][j+1])

  print(dp[0][0])

Solve()
