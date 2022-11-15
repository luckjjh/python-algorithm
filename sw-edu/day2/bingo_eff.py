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


def Solve():
  pos_bingo=[0]*26
  for i in range(len(map_bingo)):
    for j in range(len(map_bingo)):
      pos_bingo[map_bingo[i][j]] = (i,j)
  cntR = [0]*5
  cntC = [0]*5
  cnt = 0
  cntCross1 = 0
  cntCross2 = 0
  for c,seq in enumerate(seq_bingo,1):
    row,col = pos_bingo[seq]
    cntR[row]+=1
    cntC[col]+=1
    if cntR[row]==5:
      cnt+=1
    if cntC[col]==5:
      cnt+=1
    if row==col:
      cntCross1+=1
      if cntCross1==5:
        cnt+=1
    if row==4-col:
      cntCross2+=1
      if cntCross2==5:
        cnt+=1
    if cnt>=3:
      print(c)
      return

Solve()