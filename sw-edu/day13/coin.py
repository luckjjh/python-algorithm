import sys


def Input_Data():
	readl = sys.stdin.readline
	W = int(readl())
	cnt = list(map(int,readl().split()))
	return W, cnt


sol, sol_cnt = -1, [0] * 6
W, cnt = Input_Data()

coin = [500,100,50,10,5,1]


def Solve():
  sumCoin = 0
  for i in range(len(coin)):
    sumCoin+=coin[i]*cnt[i]
  remain = sumCoin-W
  for i in range(len(coin)):
    temp = min(remain//coin[i],cnt[i])
    cnt[i]-=temp
    remain-=coin[i]*temp
  print(sum(cnt))
  print(*cnt)

Solve()