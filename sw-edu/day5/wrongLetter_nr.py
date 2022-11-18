import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    str_input = readl()[:-1]
    return str_input


sol = 0

str_input = input_data()

def checkIsValid(arr):
  stack = deque()
  for i in arr:
    if i=="(":
      stack.append("(")
    elif i==")":
      if not stack:
        return False
      if stack[-1]=="(":
        stack.pop()
  return True

def Solve():
  strArr = list(str_input.rstrip())
  cnt=cntOpen=cntClose = 0
  ans = 0
  if checkIsValid(strArr):
    print(0)
    return
  for i in range(len(strArr)):
    if strArr[i]=="(":
      cnt+=1
      cntOpen+=1
    else:
      cnt-=1
      cntClose+=1
    if cnt==-1:
      ans = cntClose
      break
    if cnt==1:
      cntOpen=0
  if cnt==2:
    ans = cntOpen
  print(ans)


Solve()
