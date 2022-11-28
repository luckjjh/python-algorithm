import sys


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = list(map(int, readl().split()))
	V = list(map(int, readl().split()))
	A = int(readl())
	return N, W, V ,A



sol, sol_cnt = -1, [0] * 7
N, W, V, A = Input_Data()
maxScore = -1
ansArr = []

def Check(arr):
  numDict = dict()
  for i in range(7):
    numDict[i] = 0
  for i in arr:
    numDict[i]+=1
  curSum = 0
  for key,value in numDict.items():
    if value>=5:
      curSum+=V[key]*value
    else:
      curSum+=W[key]*value
  curSum+=len(arr)*A
  return curSum,list(numDict.values())

def Solve(curSum,arr,start):
  global maxScore,ansArr
  if curSum==N:
    curS,curA = Check(arr)
    if maxScore<curS:
      maxScore = curS
      ansArr = curA.copy()
    return
  for i in range(start,N):
    nextSum = curSum+pow(2,i)
    if nextSum<=N:
      arr.append(i)
      Solve(nextSum,arr,i)
      arr.pop(-1)
    else:
      break
ans = []

Solve(0,ans,0)
print(maxScore)
print(*ansArr)