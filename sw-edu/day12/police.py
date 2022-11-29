import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = int(readl())
	pos = [list(map(int, readl().split())) for n in range(W)]
	return N, W, pos


sol = -1
N, W, pos = Input_Data()

minDist = 987654321

def Solve(level,car1,car2,curDist):
  global minDist
  if level==W:
    minDist = min(curDist,minDist)
    return
  if minDist<=curDist:
    return
  car1Dist = abs(pos[level][0]-car1[0])+abs(pos[level][1]-car1[1])
  car2Dist = abs(pos[level][0]-car2[0])+abs(pos[level][1]-car2[1])
  nextDist = (pos[level][0],pos[level][1])
  Solve(level+1,nextDist,car2,curDist+car1Dist)
  Solve(level+1,car1,nextDist,curDist+car2Dist)


Solve(0,(1,1),(N,N),0)

print(minDist)