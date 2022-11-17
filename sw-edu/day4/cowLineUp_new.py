import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = 9876543210

# 입력받는 부분
N, info = Input_Data()
cow = [0]*(N+1)
# 여기서부터 작성
num = dict()
# 번호 재지정
n = 1
allcount = 0
for i in range(N):
    if not (info[i][1] in num):
        num[info[i][1]] = n
        n += 1
        allcount += 1
    info[i][1] = num[info[i][1]]

info.sort(key=lambda x: x[0])
print(info)
cnt = 0
carr = [0]*(N+1)

s = 0

for e in range(N):
    print(carr,cnt)
    carr[info[e][1]] += 1
    if carr[info[e][1]] == 1:
        cnt += 1

    while carr[info[s][1]] >= 2:
        carr[info[s][1]] -= 1
        s += 1

    if cnt == allcount:
        sol = min(sol, info[e][0]-info[s][0])
        carr[info[s][1]] -= 1
        if carr[info[s][1]] == 0:
            cnt -= 1
        s += 1
# 출력하는 부분
print(sol)
