import sys

def Input_data():
    readl = sys.stdin.readline
    N = int(input())
    return N

sol = 0

N = Input_data() 
numArr=[]
for i in str(N):
  i = int(i)
  if i<4:
    numArr.append(i)
  else:
    numArr.append(i-1)
def Solve():
  ans = 0
  for idx,i in enumerate(numArr):
    ans += i*pow(9,(len(numArr)-1-idx))
  print(ans)

Solve()