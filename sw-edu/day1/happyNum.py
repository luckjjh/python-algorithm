import sys 

def Input_Data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    return N 

sol = 0 
# 입력받는 부분 
N = Input_Data() 

# 여기서부터 작성 
def Solve():
  for i in range(N,0,-1):
    curNum = i
    ans = []
    while True:
      temp = 0
      for j in str(curNum):
        temp+=pow(int(j),2)
      curNum = temp
      if temp in ans:
        break
      ans.append(temp)
      if temp==1:
        print(i)
        return

# 출력하는 부분 
Solve()