import sys 

def Input_Data(): 
    readl = sys.stdin.readline 
    K = int(readl()) 
    N = int(readl()) 
    info = [readl().split() for _ in range(N)] 
    info = [(int(t), z) for t,z in info] 
    return K, N, info 

# 입력받는 부분 
K, N, info = Input_Data() 
sol = 0 
# 여기서부터 작성 

def Solve():
  curPerson = K
  curTime = 0
  for time, ans in info:
    curTime+=time
    if curTime >=210:
      print(curPerson)
      return
    if ans == "T":
      curPerson+=1
      if curPerson>8:
        curPerson=1

  print(curPerson)

# 출력하는 부분 
Solve()