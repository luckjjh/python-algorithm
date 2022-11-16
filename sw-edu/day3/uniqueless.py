import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    words = readl().split()
    return N, words

N, words = Input_Data()

def Solve():
  di = dict()
  for idx, word in enumerate(words,1):
    if word in di:
      di[word].append(idx)
    else:
      di[word] = [idx]
  check = True
  for i in di:
    if len(di[i])>1:
      check = False
      print(i,end=" ")
      print(*di[i])
  if check:
    print("unique")

Solve()