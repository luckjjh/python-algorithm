import sys
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info
sol = -1
N, info = input_data()
iArr = []
for i in range(len(info)):
  iArr.append((info[i][0]*100+info[i][1],info[i][2]*100+info[i][3]))
iArr.sort()
def Solve():
    info
    cnt = 0
    e = 301                                                     
    i = 0                                                       
    while e <= 1130:                                        
        max_e = 0                                              
        while i<N and iArr[i][0] <= e:                        
            max_e = max(max_e, iArr[i][1])                  
            i+=1
        if max_e <= e: 
          print(0)
          return
        cnt+=1                                                
        e = max_e
    print(cnt)
Solve()