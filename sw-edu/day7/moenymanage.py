import sys
import bisect

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int,readl().split())
	need = [int(readl()) for _ in range(N)]
	return N, M, need

sol = -1

N, M, need = Input_Data()

sumMoney = sum(need)

def Solve():
  low = 0
  high = sumMoney
  while low<=high:
    mid = (high+low)//2
    cnt = 1
    curMoney = mid
    for i in range(len(need)):
      if curMoney<need[i]:
        curMoney=mid
        cnt+=1
      curMoney-=need[i]

    if cnt>M or mid<max(need):
      low = mid+1
    else:
      high = mid-1
      ans = mid
  print(ans)


Solve()