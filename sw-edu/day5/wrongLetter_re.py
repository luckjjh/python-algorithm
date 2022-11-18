import sys


def input_data():

    readl = sys.stdin.readline

    str_input = readl()[:-1]

    return str_input


sol = 0


str_input = input_data()

def Solve():
  global sol
  openCnt = 0
  cnt = 0
  closeCnt = 0
  for i in str_input:
    if i=="(":
      cnt+=1
      openCnt+=1
    else:
      cnt-=1
      closeCnt+=1

    if cnt < 0:
      sol = closeCnt
      break
    if cnt <=1:
      openCnt = 0
  else:
    sol = openCnt
  print(sol)
Solve()