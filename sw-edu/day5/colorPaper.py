import sys 

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    info = [list(map(int, readl().split())) for _ in range(N)] 
    return N, info

sol = 0 

N, info = input_data() 

maps = [[0]*102 for _ in range(102)]

for row,col in info:
  for i in range(10):
    for j in range(10):
      maps[row+i][col+j]=1

for i in range(102):
  for j in range(102):
    if maps[i][j]>0:
      maps[i][j]+=maps[i-1][j]

maxSize = -1

def Solve():
  global maxSize

  for i in range(102):
    for j in range(102):
      if maps[i][j]>0:
        curRow = i
        curCol = j
        width = 0
        length = maps[i][j]
        while maps[curRow][curCol]>0:
          width+=1
          length = min(length,maps[curRow][curCol])
          maxSize = max(maxSize,width*length)
          curCol+=1
        maxSize = max(maxSize,width*length)
  print(maxSize)
Solve()