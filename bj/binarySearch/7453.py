import sys
import bisect


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    nuMap = [list(map(int, readl().split())) for _ in range(N)]
    return N, nuMap


N, nuMap = Input_Data()

# abdict = dict()
# result = 0


# def Solve():
#     global result
#     for i in range(N):
#         for j in range(N):
#             v = nuMap[i][0]+nuMap[j][1]
#             if v not in abdict.keys():
#                 abdict[v] = 1
#             else:
#                 abdict[v] = -1

#     for i in range(N):
#         for j in range(N):
#             v = -1 * (nuMap[i][2]+nuMap[j][3])
#             if v in abdict.keys():
#                 result += abdict[v]

#     print(result)


# Solve()


abList = []
cdList = []


def Solve():
    cnt = 0
    for i in range(N):
        for j in range(N):
            abList.append(nuMap[i][0]+nuMap[j][1])
            cdList.append(nuMap[i][2]+nuMap[j][3])
    abList.sort()
    cdList.sort()

    left = 0
    right = len(cdList)-1
    while left < len(cdList) and right >= 0:
        curSum = abList[left]+cdList[right]
        if curSum > 0:
            right -= 1
        elif curSum < 0:
            left += 1
        else:
            abLow = bisect.bisect_left(abList, abList[left])
            abHigh = bisect.bisect_right(abList, abList[left])
            cdLow = bisect.bisect_left(cdList, cdList[right])
            cdHigh = bisect.bisect_right(cdList, cdList[right])
            cnt += (abHigh-abLow)*(cdHigh-cdLow)  # 같은 숫자들 경우의 수 만들어 줌
            left = abHigh
            right = cdLow-1
    print(cnt)


Solve()
