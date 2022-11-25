import sys
from collections import deque
  
def Input_Data():
    readl = sys.stdin.readline
    return [['.']+list(readl().strip())+['.'] if 1 <= r <= 12 else ['.'] * 8 for r in range(14)]
  
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
  
def Flood_Fill_Count(chk, sr, sc):
    color = map_puyo[sr][sc]
    cnt_conn = 1
    q = deque()
    q.append((sr, sc))
    list_conn = deque()
    list_conn.append((sr,sc))
    chk[sr][sc] = 1
    while q:
        r,c = q.popleft()
        for dr,dc in d:
            nr, nc = r + dr, c + dc
            if map_puyo[nr][nc] != color or chk[nr][nc] == 1: continue
            chk[nr][nc] = 1
            cnt_conn += 1
            q.append((nr, nc))
            list_conn.append((nr,nc))
    return cnt_conn, list_conn

def Flood_Fill_Erase(list_conn):
    for r,c in list_conn:
        map_puyo[r][c] = '.'

def Find_Connection():
    cnt_erase = 0
    chk = [[0] * 8 for _ in range(14)]
    for r in range(1, 12 + 1):
        for c in range(1, 6 + 1):
            if map_puyo[r][c] == '.': continue
            if chk[r][c] == 1: continue
            cnt_conn, list_conn = Flood_Fill_Count(chk, r, c)
            if cnt_conn<4: continue
            Flood_Fill_Erase(list_conn)
            cnt_erase += 1
    return cnt_erase
   
   
def Down_Puyo():
    for c in range(1,7):
        r_space, r_puyo = 12,-1
        while 1:
            while r_space>=1 and map_puyo[r_space][c] != '.': r_space-=1
            if r_space == 0: break
            if r_puyo == -1: r_puyo = r_space-1
            while r_puyo >= 1 and map_puyo[r_puyo][c] == '.': r_puyo-=1
            if r_puyo == 0: break
            map_puyo[r_space][c] = map_puyo[r_puyo][c]
            map_puyo[r_puyo][c] = '.'
            r_space -= 1
   
def Solve():
    combo = 0
    while 1:
        if Find_Connection()==0:
            break
        combo += 1
        Down_Puyo()
    return combo
  
  
T = int(input())
sol = []
for _ in range(T):
    map_puyo = Input_Data()
    sol.append(Solve())

print(*sol, sep='\n')