import sys
import bisect

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	list_file = list(map(int, readl().split()))
	return N, list_file


sol = 0


N, list_file = Input_Data()
list_file.sort()

def Solve():
  global sol
  for i in range(len(list_file)-1):
    curScore = list_file[i]
    curMax = curScore/0.9
    right = bisect.bisect_right(list_file,curMax)
    sol+=(right-(i+1))
  print(sol)
Solve()