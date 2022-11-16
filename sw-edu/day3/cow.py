import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    str_input = readl()[:-1]
    return str_input

sol = 0

str_input = Input_Data()


def Solve():
  cnt = 0
  stack = deque()
  for i in str_input:
    if i == "(":
      if not stack or stack[-1]=="(":
        stack.append(i)
    if i == ")":
      if stack and stack[-1]=="(":
        stack.pop()
      elif not stack:
        cnt+=1
        stack.append("(")
      else:
        cnt+=1
  
  cnt = cnt+len(stack)//2
  print(cnt)

Solve()