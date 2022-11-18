import sys 

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    chems = [list(map(int,readl().split())) for _ in range(N)] 
    return N, chems 

sol = 0 

N, chems = input_data() 

chems.sort(key=lambda i:i[1])

def Solve():
  lastTemp = chems[0][1]
  refCnt = 1
  for i in range(1,len(chems)):
    if lastTemp<chems[i][0]:
      refCnt+=1
      lastTemp=chems[i][1]
  print(refCnt)


Solve()