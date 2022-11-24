import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int,readl().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
    return N, r_top, c_top, map_mountine


sol = -1

N, r_top, c_top, map_mountine = Input_Data()

check = [[987654321]*(N+2)for _ in range(N+2)]


def Solve():
  q = deque()
  q.append((0,0,0))
  check[0][0] = 0
  dir = ((-1,0),(1,0),(0,-1),(0,1))
  while q:
    curRow,curCol,curStren = q.popleft()
    if check[curRow][curCol]<curStren:
      continue
    for r_d,c_d in dir:
      nextRow,nextCol = curRow+r_d,curCol+c_d
      if nextRow<0 or nextCol<0:
        continue
      if nextRow>N+1 or nextCol>N+1:
        continue
      diff = map_mountine[curRow][curCol]-map_mountine[nextRow][nextCol]
      if diff<0:
        nextSum = curStren+diff**2
      else:
        nextSum = curStren+diff

      if check[nextRow][nextCol]<=nextSum:
        continue
      check[nextRow][nextCol] = nextSum
      q.append((nextRow,nextCol,nextSum))
  print(check[r_top][c_top])

Solve()