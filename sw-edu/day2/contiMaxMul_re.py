import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [float(readl()) for _ in range(N)]
    return N, num

sol = 0.0
N, num = Input_Data()


def Solve():
  for i in range(1,len(num)):
    num[i]=max(num[i],num[i]*num[i-1])
  print(f"{max(num):.3f}") 

Solve()