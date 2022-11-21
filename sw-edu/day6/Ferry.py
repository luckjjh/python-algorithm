import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    M, T, N = map(int,readl().split())
    info = [list(readl().split()) for _ in range(N)]
    info = [[i, int(s[0]), s[1]] for i, s in enumerate(info)]
    return M, T, N, info

ans = []

M, T, N, info = Input_Data()
def Solve():
  leftQ = deque()
  rightQ = deque()
  curDir = 0 # 0 left / 1 right
  curTime = 0
  for id,time,dir in info:
    if dir=="left":
      leftQ.append((id,time))
    else:
      rightQ.append((id,time))

  while leftQ or rightQ:
    check = True
    if leftQ and leftQ[0][1]<=curTime:
      check = False
      if curDir==0:
        curDir=1
        cnt = 0
        while leftQ and leftQ[0][1]<=curTime and cnt<M:
          tempId,tempTime = leftQ.popleft()
          ans.append((tempId,curTime+T))
          cnt+=1
        curTime+=T
      else:
        curTime+=T
        cnt = 0
        while leftQ and leftQ[0][1]<=curTime and cnt<M:
          tempId,tempTime = leftQ.popleft()
          ans.append((tempId,curTime+T))
          cnt+=1
        curTime+=T
    if rightQ and rightQ[0][1]<=curTime:
      check = False
      if curDir==1:
        curDir = 0
        cnt = 0
        while rightQ and rightQ[0][1]<=curTime and cnt<M:
          tempId,tempTime = rightQ.popleft()
          ans.append((tempId,curTime+T))
          cnt+=1
        curTime+=T
      else:
        curTime+=T
        cnt = 0
        while rightQ and rightQ[0][1]<=curTime and cnt<M:
          tempId,tempTime = rightQ.popleft()
          ans.append((tempId,curTime+T))
          cnt+=1
        curTime+=T
    if check:
      curTime+=1
  
  ans.sort(key=lambda i:i[0])
  for i,j in ans:
    print(j)


Solve()