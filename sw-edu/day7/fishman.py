import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info
# N 마을 수
# A 도시 위치, B 잡힌 물고기


sol = -1

N, info = Input_Data()

fishArr=[]
gapArr=[]
for id,fish in info:
  fishArr.append(fish)

for i in range(len(info)-1):
  gapArr.append(info[i+1][0]-info[i][0])

sumGap = sum(gapArr)
sumGap = -sumGap
def Solve():
  global sol
  low = 0
  high = max(fishArr)
  while low<=high:
    mid = (low+high)//2
    cnt = 0
    for i in range(len(fishArr)-1):
      remain = fishArr[i]+cnt-mid
      cnt=remain-(info[i+1][0] - info[i][0])
      if remain>=0 and cnt<0:
        cnt = 0
    if info[N-1][1]+cnt>=mid:
      low = mid+1
      sol = mid
    else:
      high = mid-1
  if sol==-1:
    print(min(fishArr))
  else:
    print(sol)


Solve()