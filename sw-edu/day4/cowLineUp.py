import sys
from collections import deque

def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  cowList = [list(map(int,readl().split())) for _ in range(N)]
  return N,cowList

N,cowList = Input_Data()

cowList.sort(key=lambda i:i[0])

minDis = sys.maxsize

def Solve():
  global minDis
  cowSet = set()
  cntDict = dict()
  for i in range(len(cowList)):
    # 소개수
    cowSet.add(cowList[i][1])
    cntDict[cowList[i][1]] = 0
  cows = len(cowSet)

  if cows==1:
    print(0)
    return
  
  cnt=0
  left = 0
  for i in range(len(cowList)):
    cntDict[cowList[i][1]]+=1

    if cntDict[cowList[i][1]]==1: # 새로들어온 소 카운트
      cnt+=1
      
    if cnt==cows:
      while cntDict[cowList[left][1]]>1:  
        # 제일 앞에 있는 소가 1마리 이상이면 1개될때 까지 제거
        cntDict[cowList[left][1]]-=1
        left+=1
      minDis = min(minDis,cowList[i][0]-cowList[left][0])
      # 검사 한 애는 하나 제거
      cntDict[cowList[left][1]]-=1
      if cntDict[cowList[left][1]]==0:
        cnt-=1
      left+=1

  print(minDis)
Solve()