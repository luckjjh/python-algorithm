import sys
  
def Input_Data():
    readl = sys.stdin.readline
    N, L, M = map(int,   readl().split())
    list_pos = [tuple(map(int, readl().split())) for _ in range(M)]
    return N, L, M, list_pos
  
N, L, M, list_pos = Input_Data()

maps = [[0]*N for _ in range(N)]
for i,j in list_pos:
  maps[i-1][j-1] = 1
for i in maps:
  print(i)

# def Solve():
