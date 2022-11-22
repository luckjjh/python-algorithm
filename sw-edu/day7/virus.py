import sys

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int,readl().split())
	intvals = [list(map(int,readl().split())) for _ in range(M)]
	return N, M, intvals


sol = -1
N, M, intvals = Input_Data()
intvals.sort(key=lambda i: i[0])


def Solve():
  global sol
  left = 1
  right = intvals[-1][1]-intvals[0][0]
  while left<=right:
    mid = (left+right)//2
    cur = intvals[0][0]
    cnt = 1
    for i in range(len(intvals)):
      s,e = intvals[i][0],intvals[i][1]
      while cur+mid<=e:
        cur = max(s,cur+mid)
        cnt+=1
    if cnt>=N:
      sol = mid
      left = mid+1
    else:
      right = mid-1
  print(sol)



Solve()