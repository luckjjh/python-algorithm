import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num

sol = -1
N, K, num = Input_Data()

def Solve():
  stack = deque()
  cnt = 0
  for i in num:
    while stack and stack[-1]<i and cnt<K:
      stack.pop()
      cnt+=1
    stack.append(i)
  while len(stack)>N-K:
    stack.pop()
  print(*stack,sep="",end="")
Solve()