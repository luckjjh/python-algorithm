import sys
from collections import deque


def Input_data():
    readl = sys.stdin.readline
    N, *list_height = map(int,readl().split())
    return N, list_height


sol = []


def Solve():
  maxSize = -1
  stack = deque()
  stack.append((0,0))
  for i in range(len(list_height)):
    lastIdx = i
    while stack and stack[-1][0]>=list_height[i]:
      h,lastIdx = stack.pop()
      tempSize = h*(i-lastIdx)
      maxSize = max(maxSize,tempSize)
    stack.append((list_height[i],lastIdx))
  for height,idx in stack:
    maxSize = max(maxSize,(N-idx)*height)
  print(maxSize)



while True:
    N, list_height = Input_data()
    if N == 0: break
    Solve()