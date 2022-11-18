import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    str_input = readl()[:-1]
    return str_input


sol = 0

str_input = input_data()

def Solve():
  strArr = list(str_input.rstrip())
  cnt=cntOpen=cntClose = 0
  ans = 0
  for i in range(len(strArr)):
    if strArr[i]=="(":
      cnt+=1
      cntOpen+=1
    else:
      cnt-=1
      cntClose+=1
    if cnt<0:
      ans = cntClose
      break
    if cnt<=1:
      cntOpen=0
  else:
    ans = cntOpen

  print(ans)


Solve()
