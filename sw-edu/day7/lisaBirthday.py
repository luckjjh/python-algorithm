import sys
import math
def Input_Data():
  readl = sys.stdin.readline
  N,M = map(int,readl().split())
  # 재료 개수, 리사 돈
  ingreList = [list(map(int,readl().split())) for _ in range(N)]
  # 완성 위해 필요 양, 현재 주방에 있는양
  # 작은 포장에 담긴 재료 양, 재료 가격
  # 큰포장에 담겨있는 재료 양, 재료 가격
  return N,M,ingreList

N,M,ingreList = Input_Data()

def Solve():
  global sol
  left = 0
  right = 100000
  while left<=right:
    mid = (left+right)//2
    curMoney = M
    check = True
    for i in range(len(ingreList)):
      toMake,remain,small,smallCost,big,bigCost = ingreList[i]
      curNeed = mid * toMake - remain 
      # mid개 만큼 만드는 데 필요한 양에서 주방에 있는 양 빼서 현재 필요한 양 계산
      curMin = sys.maxsize
      for j in range(curNeed//small+2):
        k = math.ceil((curNeed - small * j)/big)
        # 재료가 남게 사야되므로 올림 연산
        if k<0:
          k = 0
        # big 살때 k 0인 경우 고려
        if j*smallCost+k*bigCost<curMin:
          curMin = j*smallCost+k*bigCost
      curMoney -= curMin
      if curMoney<0:
        check = False
        break
    if check:
      left = mid+1
    else:
      right = mid -1
  print(right)


      

Solve()