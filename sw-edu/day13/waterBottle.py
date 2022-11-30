import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    A, B, C, D = map(int,readl().split())
    return A, B, C, D

sol = -2
A, B, C, D = Input_Data()
# a용량 b 용량 a에 남겨야되는 양 b에 남겨야되는양

def Solve():
  q = deque()
  q.append((0,0,0))
  visit = [[0]*(B+1) for _ in range(A+1)]
  while q:
    curA,curB,cnt = q.popleft()
    if visit[curA][curB]:
      continue
    visit[curA][curB]=cnt
    q.append((A,curB,cnt+1))
    q.append((curA,B,cnt+1))
    q.append((0,curB,cnt+1))
    q.append((curA,0,cnt+1))
    if curA<=B-curB:
      q.append((0,curB+curA,cnt+1))
    else:
      q.append((curA-(B-curB),B,cnt+1))
    if curB<=A-curA:
      q.append((curA+curB,0,cnt+1))
    else:
      q.append((A,curB-(A-curA),cnt+1))
  if visit[C][D]==0:
    print(-1)
    return
  print(visit[C][D])

Solve()