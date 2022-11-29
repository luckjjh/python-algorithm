import sys

def input_data():
    map_soli = [[0] + list(readl().strip()) + [0] if 1<=r<=5 else [0]*11 for r in range(7)]
    readl()
    return map_soli

dir = ((-1,0),(1,0),(0,-1),(0,1))


def DFS(row,col,pCnt,move):
  global curMin,moveMin
  if pCnt<=curMin:
    curMin = pCnt
    moveMin = move
  for r_d,c_d in dir:
    nextRow,nextCol = row+r_d,col+c_d
    if 1<=nextRow<=5 and 1<=nextCol<=9 and map_soli[nextRow][nextCol]=='o':
      nnRow,nnCol = nextRow+r_d,nextCol+c_d
      if 1<=nnRow<=5 and 1<=nnCol<=9 and map_soli[nnRow][nnCol]=='.':
        map_soli[row][col] = '.'
        map_soli[nextRow][nextCol] = '.'
        map_soli[nnRow][nnCol] = 'o'
        for i in range(1,6):
          for j in range(1,10):
            if map_soli[i][j]=='o':
              DFS(i,j,pCnt-1,move+1)
        map_soli[row][col] = 'o'
        map_soli[nextRow][nextCol] = 'o'
        map_soli[nnRow][nnCol] = '.'


def Solve():
  pinArr = []
  for i in range(1,6):
    for j in range(1,10):
      if map_soli[i][j]=='o':
        pinArr.append((i,j))
  pinCnt = len(pinArr)
  for i in range(1,6):
    for j in range(1,10):
      if map_soli[i][j]=='o':
        DFS(i,j,pinCnt,0)


readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    curMin = 987654321
    moveMin = 987654321
    map_soli = input_data()
    Solve()
    print(curMin,moveMin)