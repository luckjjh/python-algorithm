import sys
from collections import deque


def Input_Data():
  readl = sys.stdin.readline
  inputStr = list(readl().rstrip())
  boom = readl().rstrip()
  return inputStr,boom

inputStr,boom = Input_Data()

def Check():
  boomr = list(boom.rstrip())
  boomr.reverse()
  idx = -1
  for i in boomr:
    if i != stack[idx]:
      return False
    idx-=1
  return True

stack = deque()

def Solve():
  global stack
  for i in inputStr:
    stack.append(i)
    if stack[-1]==boom[-1]:
      if Check():
        for i in range(len(boom)):
          stack.pop()

  if stack:
    print(*stack,sep="")
  else:
    print("FRULA")

Solve()