import sys

def input_data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N+1)]
    return N, W, H, info

sol = -1


N, W, H, info = input_data()
# 1 북, 2 남, 3 서, 4 동


def Solve():
  cnt = 0
  distArr = []
  for i in range(N+1):
    dir,pos = info[i]
    if dir==1:
      distArr.append(pos)
    elif dir==2:
      distArr.append((W-pos)+H+W)
    elif dir==3:
      distArr.append(H+W+W+(H-pos))
    elif dir==4:
      distArr.append(W+pos)
  curDist = distArr.pop(-1)
  for i in range(N):
    indiff = abs(curDist-distArr[i])
    outdiff = W+W+H+H-indiff
    cnt+=min(indiff,outdiff)
  print(cnt)

Solve()
