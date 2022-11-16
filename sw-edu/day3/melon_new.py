import sys

def Input_Data():
    readl = sys.stdin.readline
    K = int(readl())
    edges = [list(map(int,readl().split()))[1] for _ in range(6)]
    return K, edges

sol = 0
K, edges = Input_Data()

def Solve():
    maxidx = max(range(6), key = lambda x:edges[x])
    x, y  = (maxidx+1)%6, (maxidx-1+6)%6
  
    if edges[x] < edges[y]:
        big_e1, big_e2 = edges[maxidx], edges[y]
        small_e1, small_e2 = edges[(maxidx-3+6)%6], edges[(maxidx-4+6)%6]
    else: 
        big_e1, big_e2 = edges[maxidx], edges[x]
        small_e1, small_e2 = edges[(maxidx+3)%6], edges[(maxidx+4)%6]
  
    area = big_e1 * big_e2 - small_e1 * small_e2
    print(area*K)

Solve()