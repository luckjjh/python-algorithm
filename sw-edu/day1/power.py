import sys 

def Input_Data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    nums = [int(readl()) for _ in range(N)] 
    return N, nums 

sol = -1
ans = -1
# 입력받는 부분 
N, nums = Input_Data() 


# 여기서부터 작성 
def Solve():
  global ans
  global sol
  for num in nums:
    temp = num
    while temp>=10:
      sum = 0
      for i in str(temp):
        sum+=int(i)
      temp = sum
    if temp>sol:
      sol = temp
      ans = num
    elif temp==sol:
      ans = min(ans,num)
  print(ans)
# 출력하는 부분 
Solve()