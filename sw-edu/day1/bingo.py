import sys 

def Input_Data(): 
    readl = sys.stdin.readline 
    map_bingo = [list(map(int, readl().split())) for _ in range(5)] 
    seq_bingo = [] 
    for _ in range(5): 
        seq_bingo += list(map(int,readl().split()))     
    return map_bingo, seq_bingo 

sol = 0 
map_bingo, seq_bingo = Input_Data() 

def Check(): # 빙고 검사
  bcnt = 0 # 빙고 개수
  for i in range(len(map_bingo)): # 가로세로 빙고 검사
    checkRow = True
    checkCol = True
    for j in range(len(map_bingo)):
      if map_bingo[i][j]>0:# 가로검사
        checkRow=False
      if map_bingo[j][i]>0:# 세로검사
        checkCol=False
    if checkRow:
      bcnt+=1
    if checkCol:
      bcnt+=1

  checkCross1=True
  checkCross2=True

  for i in range(len(map_bingo)):# 대각선 빙고 검사
    if map_bingo[i][i]>0:
      checkCross1=False
    if map_bingo[(len(map_bingo)-1)-i][i]>0:
      checkCross2=False

  if checkCross1:
    bcnt+=1
  if checkCross2:
    bcnt+=1
  
  if bcnt>=3:
    return True
  else:
    return False

def Solve():
  global map_bingo
  cnt = 0
  for seq in seq_bingo:
    for i in range(len(map_bingo)):
      for j in range(len(map_bingo)):
        if map_bingo[i][j]==seq:
          map_bingo[i][j] = -1
    cnt+=1
    if Check():
      print(cnt)
      return

Solve()