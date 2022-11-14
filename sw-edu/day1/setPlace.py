import sys

def Input_Data():
  readl = sys.stdin.readline
  Col,Row = map(int,readl().split())
  N = int(readl())
  return Col,Row,N


Col,Row,N = Input_Data()

maps = [[0]*Col for _ in range(Row)]

def Solve():
  dir = ((1,0),(0,1),(-1,0),(0,-1)) # CCW 방향 하, 우, 상, 좌
  curDir = 0
  curRow,curCol = 0,0
  maps[curRow][curCol] = 1
  
  if Col*Row<N: # 가로x세로보다 N이 크면 N은 자리배치 못함
    print(0)
    return

  for i in range(2,N+1):
    nextRow = curRow+dir[curDir][0]
    nextCol = curCol+dir[curDir][1]

    if not 0<=nextRow<Row or not 0<=nextCol<Col or maps[nextRow][nextCol]!=0:
      curDir=(curDir+1)%4
      nextRow = curRow+dir[curDir][0]
      nextCol = curCol+dir[curDir][1]

    curRow = nextRow
    curCol = nextCol
    maps[curRow][curCol]=i
  print(curCol+1,curRow+1)
  return
Solve()