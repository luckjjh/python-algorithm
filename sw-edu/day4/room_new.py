import sys 

def Input_Data(): 
    N = int(sys.stdin.readline()) 
    list_meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
    return N, list_meeting 

N, list_meeting = Input_Data() 

list_meeting.sort(key=lambda i:(i[2],i[1]))

def Solve():
  ans = []
  ans.append(list_meeting[0])
  for idx in range(1,len(list_meeting)):
    if ans[-1][2]<=list_meeting[idx][1]:
      ans.append(list_meeting[idx])

  print(len(ans))
  for i,s,e in ans:
    print(i,end=" ")

Solve()