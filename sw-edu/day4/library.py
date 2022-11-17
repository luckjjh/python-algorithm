import sys

def Input_Data():
    N = int(sys.stdin.readline())
    list_time = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]    
    return N, list_time

sol = [-1, -1]
N, list_time = Input_Data()

list_time.sort(key=lambda i: i[0])

curMax = -1
outMax = -1
def Solve():
  global curMax,outMax
  lastTimeIn = list_time[0][0]
  lastTimeOut = list_time[0][1]
  for i in range(1,len(list_time)):
    if list_time[i][0]<=lastTimeOut:
      if lastTimeOut < list_time[i][1]:
        lastTimeOut = list_time[i][1]
      curMax=max(curMax,lastTimeOut-lastTimeIn)
    else:
      if outMax<list_time[i][0]-lastTimeOut:
        outMax = list_time[i][0]-lastTimeOut
      lastTimeIn = list_time[i][0]
      lastTimeOut = list_time[i][1]
  print(curMax,outMax)

Solve()