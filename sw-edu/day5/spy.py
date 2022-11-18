import sys 
from collections import deque

def input_data(): 
    readl = sys.stdin.readline 
    N, str_org = readl().split() 
    return int(N), str_org 

sol = [] 

N, str_org = input_data() 
levelList = []
def Solve():
  stack = deque()
  level = 0
  for i in str_org:
    if i.isdigit() or i=="<":
      if i=="<":
        level+=1
      stack.append(i)
    if i ==">":
      if stack[-1]=="<":
        stack.pop()
      else:
        curName = ""
        while stack[-1].isdigit():
          curName+=stack[-1]
          stack.pop()
        levelList.append(("".join(reversed(curName)),level))
        stack.pop()
      level-=1
  for name,level in levelList:
    if level==N:
      print(name,end=" ")
  

Solve()