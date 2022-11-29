import sys
from itertools import permutations

def input_data():
    readl = sys.stdin.readline
    B, N = map(int, readl().split())
    weight_ship = [int(readl()) for _ in range(B)]
    weight_passenger = [int(readl()) for _ in range(N)]
    return B, N, weight_ship, weight_passenger


maxW = -1

B, N, weight_ship, weight_passenger = input_data()
# 배 수, 승객 수, 각 배 최대 수용 무게, 각 승객 무게
pwArr = [0]*(N+1)
canRide = [0]*B

def DFS(level,cnt,sumShip):
  global maxW
  if sumShip<=maxW:
    return
  if level==N:
    maxW = sumShip
    return

  for i in range(B):
    if canRide[i]:
      continue
    last = Check(cnt,weight_ship[i])
    if last==-1:
      continue
    canRide[i]=1
    DFS(level+(last-cnt),last,sumShip-weight_ship[i])
    canRide[i]=0


def Check(cnt,p):
  ans = -1
  low = cnt
  high = N
  while low<=high:
    mid = (high+low)//2
    weight = pwArr[mid]-pwArr[cnt]
    if weight>p:
      high=mid-1
    elif weight==p:
      return mid
    else:
      low = mid+1
      ans = mid
  return ans


def Solve():
  if sum(weight_passenger)>sum(weight_ship):
    print(-1)
    return
  for i in range(len(weight_passenger)):
    pwArr[i+1] = pwArr[i]+weight_passenger[i]
  # print(pwArr)
  DFS(0,0,sum(weight_ship))

  print(maxW)


Solve()