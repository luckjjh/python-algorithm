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
  cnt = 1
  lastTemp = chems[0][1]
  for idx in range(1,len(chems)):
    if lastTemp<chems[idx][0]:
      cnt+=1
      lastTemp = chems[idx][1]


  print(cnt)
Solve()