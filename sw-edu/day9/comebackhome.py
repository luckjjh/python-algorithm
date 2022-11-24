import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    P = int(readl())
    infos = [(lambda x:[x[0],x[1],int(x[2])]) (readl().split()) for _ in range(P)]
    return P, infos


sol_pos, sol_dist = -1, -1
P, infos = Input_Data()
startArr = []

minCnt = sys.maxsize
lastPos = ""

for start,end,cost in infos:
  if start=="Z" or end=="Z":
    continue
  if start.isupper():
    startArr.append(start)
  if end.isupper():
    startArr.append(end)
startArr = list(set(startArr))

def Solve(startPos):
  global lastPos,minCnt
  cowDict = dict()
  for s,e,c in infos:
    cowDict[s] = sys.maxsize
    cowDict[e] = sys.maxsize
  q = deque()
  q.append((startPos,0))
  cowDict[startPos] = 0
  while q:
    curPos,cnt = q.popleft()
    if cowDict[curPos]>minCnt:
      continue
    for start,end,cost in infos:
      if start==curPos:
        if cowDict[end]<=cnt+cost:
          continue
        else:
          cowDict[end]=cnt+cost
          q.append((end,cnt+cost))
      if end==curPos:
        if cowDict[start]<=cnt+cost:
          continue
        else:
          cowDict[start]=cnt+cost
          q.append((start,cnt+cost))
  if minCnt>cowDict["Z"]:
    lastPos = startPos
    minCnt = cowDict["Z"]

def Run():
  for i in startArr:
    Solve(i)
  print(lastPos,minCnt)

Run()