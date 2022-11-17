import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	info = [list(map(int,input().split())) for _ in range(N)]
	return N, info


sol = -1
N, info = Input_Data()

info.sort(key=lambda i:(i[1],i[0]))


def Solve():
  info2 = []
  for start,end in info:
    if end-start>=2:
      info2.append((start,end))
  lastend = -1
  cnt = 0
  for start,end in info2:
    if lastend<=start:
      cnt+=1
      lastend = end
  print(cnt)

Solve()