import sys
from collections import deque
import copy
def Input_Data():
    readl = sys.stdin.readline
    S, E = map(int, readl().split())
    return S, E

visit = [0]*10000
sol = -2

S, E = Input_Data()

def isPrimeNum(num):
  for i in range(2,num-1):
    if num%i==0:
      return False
  return True

def Solve():
  q = deque()
  q.append((S,0))
  while q:
    curNum,curCnt = q.popleft()
    if curNum==E:
      print(curCnt)
      return
    curNum = list(map(int,str(curNum).strip()))
    for i in range(4): # 자리수
      nextNum = copy.deepcopy(curNum)
      for j in range(10): # 숫자
        if i==0 and j==0:
          continue
        if j==curNum[i]:
          continue
        nextNum[i]=j
        num = 0
        for k in range(4):
          num+=nextNum[k]*pow(10,3-k)
        if visit[num]:
          continue
        visit[num] = 1
        if isPrimeNum(num):
          q.append((num,curCnt+1))
Solve()