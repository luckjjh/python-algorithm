import sys
  
def Input_Data():
    readl = sys.stdin.readline
    N, L, M = map(int,   readl().split())
    list_pos = []
    for i in range(M):
      r,c = map(int,readl().split())
      list_pos.append((r-1,c-1))
    return N, L, M, list_pos
  
N, L, M, list_pos = Input_Data()
# list_pos = list(map(lambda i:(i[0]-1,i[1]-1),list_pos))
maxFish = -1

def CountFish(sRow,sCol,eRow,eCol):
  cnt = 0
  if eRow>N or eCol>N:
    return cnt
  for r,c in list_pos:
    if sRow<=r<eRow and sCol<=c<eCol:
      cnt+=1
  return cnt

def Solve():
  global maxFish
  dir = ((0,1),(1,0),(0,-1),(-1,0))
  for row,col in list_pos:
    for a in range(1,L//2):
      b = (L//2)-a
      if b>N-1 or a>N-1:
        continue
      startRow,startCol,endRow,endCol = row-a,col-b,a,b
      aCnt,bCnt = a,b
      d = 0
      while d<4:
        if d%2==1:
          startRow+=dir[d][0]
          aCnt-=1
          if not aCnt:
            aCnt = a
            d+=1
        else:
          startCol+=dir[d][1]
          bCnt-=1
          if not bCnt:
            bCnt = b
            d+=1
        if startRow>=0 and startCol>=0:
          endRow = startRow+a+1
          endCol = startCol+b+1
          maxFish = max(maxFish,CountFish(startRow,startCol,endRow,endCol))
  print(maxFish)

Solve()