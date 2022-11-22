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
    left = i+1
    right = len(list_file)-1
    cnt = -1
    while left<=right:
      mid = (right+left)//2
      if curScore/list_file[mid]<0.9:
        right = mid-1
      else:
        cnt = mid
        left = mid+1
    if cnt>-1:
      sol+=cnt-i
  print(sol)
Solve()