import sys 
# 회전 초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 
# 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가 각각 하나의 빈 칸을 
# 사이에 두고 주어진다. 
def Input_Data(): 
    read = sys.stdin.readline 
    N, d, k, c = map(int,read().split()) 
    dish = [int(read()) for _ in range(N)] 
    return N, d, k, c, dish 

N, d, k, c, dish = Input_Data()
dish += dish[:k-1]
d = int(d)
checkArr = [0]*(d+1)

def Solve():
  curmax = -1
  left = 0
  right = k-1
  for i in range(k):
    checkArr[dish[i]]+=1
  curcnt = 0
  for i in range(len(checkArr)):
    if checkArr[i]>0:
        curcnt+=1
  curmax = curcnt
  while right<len(dish)-1:
    left+=1
    right+=1
    cnt = 0
    checkArr[dish[left-1]] -= 1
    checkArr[dish[right]] += 1
    if checkArr[dish[left-1]]==0:
      cnt-=1
    if checkArr[dish[right]]==1 and dish[right]!=dish[left-1]:
      cnt+=1
    curcnt = curcnt+cnt
    if checkArr[c]==0:
      curmax = max(curmax,curcnt+1)
    else:
      curmax = max(curmax,curcnt)
  print(curmax)

Solve()