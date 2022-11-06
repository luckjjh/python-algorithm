import sys
from collections import deque

def Input_Data():
  readl = sys.stdin.readline
  N,M = map(int,readl().split())
  costs = [int(readl()) for _ in range(N)]
  weight = [int(readl()) for _ in range(M)]
  cmd = [int(readl()) for _ in range(M*2)]
  return N,M,costs,weight,cmd

N,M,costs,weight,cmd = Input_Data()
parking = [0]*N

def areaExist():
  for i in parking:
    if i==0:
      return True
  return False

def Solve():
  curCost = 0
  q = deque()
  for cm in cmd:
    if q:
        for i in range(len(parking)):
          if parking[i]==0:
            curCar = q.popleft()
            parking[i]=curCar
            curCost += weight[curCar-1]*costs[i]
    if cm>0:
      check = True
      for i in range(len(parking)):
        if parking[i]==0:
          parking[i]=cm
          curCost += weight[cm-1]*costs[i]
          check = False
          break
      if check:
        q.append(cm)
        
    elif cm<0:
      cm = -cm
      for i in range(len(parking)):
        if parking[i]==cm:
          parking[i]=0
  print(curCost)

Solve()