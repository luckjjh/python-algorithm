import sys 

def Input_Data(): 
    N = int(sys.stdin.readline()) 
    list_meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
    return N, list_meeting 


N, list_meeting = Input_Data() 

list_meeting.sort(key=lambda i:(i[2],i[1]))

def Solve():
  ans = []
  ans.append(list_meeting[0][0])
  lastEndTime = list_meeting[0][2]
  for i in range(1,len(list_meeting)):
    if list_meeting[i][1]>=lastEndTime:
      ans.append(list_meeting[i][0])
      lastEndTime = list_meeting[i][2]
  print(len(ans))
  print(*ans)

Solve()