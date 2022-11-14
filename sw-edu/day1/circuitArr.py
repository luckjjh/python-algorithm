import sys


def input_data():
    readl = sys.stdin.readline
    N, P = map(int, readl().split())
    return N, P


sol = 0
ans=[]
# 입력받는 부분

N, P = input_data()
# 여기서부터 작성 

def Solve():
  curNum = N
  while True:
    curNum = (N*curNum)%P
    if curNum in ans:
      idx = -1
      cnt=1
      while ans[idx]!=curNum:
        idx-=1
        cnt+=1
      print(cnt)
      break
    ans.append(curNum)
    
# 출력하는 부분 

Solve()