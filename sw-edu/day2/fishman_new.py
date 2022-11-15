import sys
  
def Input_Data():
    readl = sys.stdin.readline
    N, L, M = map(int,   readl().split())
    list_pos = [tuple(map(int,   readl().split())) for _ in range(M)]
    return N, L, M, list_pos
  
N, L, M, list_pos = Input_Data()
# list_pos = list(map(lambda i:(i[0]-1,i[1]-1),list_pos))

maxFish = 0
list_pos.sort()

def Solve():
  global maxFish
  for a in range(1,L//2):
    b = L//2-a
    if b>N-1 or a>N-1:
      continue
    for i in range(len(list_pos)):
      row = list_pos[i][0]
      col = list_pos[i][1]
      for j in range(b+1):
        cnt = 1
        for k in range(i+1,M):
          nextRow = list_pos[k][0]
          nextCol = list_pos[k][1]
          if nextRow>row+a:
            break
          if (col-j)<=nextCol<=(col-j+b):
            cnt+=1
        maxFish = max(maxFish,cnt)
  print(maxFish)

Solve()

