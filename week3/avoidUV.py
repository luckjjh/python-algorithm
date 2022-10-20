from multiprocessing import heap
import readline
import sys
from collections import deque
import heapq
# 영희는 자외선이 피부에 좋지 않기 때문에 이동 시 자외선에 노출되는 것을 최소한으로 하고 싶어서 가는 길의 자외선 양을 모두 조사하였다.
# 값이 제 각각이어서 어떤 경로로 가야 좋을지 난감한 영희를 도와주자.
# N*N 모양의 장소의 모든 길의 자외선 양이 주어지고 영희는 상하좌우 한 칸씩만 이동이 가능하다.
# 시작점(1,1)에서 도착점(N,N)까지 이동 시 자외선 합의 최소값을 찾아라.
# 예를 들어 3*3 장소의 자외선 양이 아래와 같다면 오른쪽처럼 이동하면 8만큼만 노출된다.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    uMap = [list(map(int, list(readl().rstrip()))) for _ in range(N)]
    return N, uMap


N, uMap = Input_Data()
minSum = 987654321


def Solve():
    global minSum
    dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
    pq = []
    q = deque()
    q.append((0, 0, 0))
    visit = [[0]*N for _ in range(N)]
    heapq.heappush(pq, (0, 0, 0))
    visit[0][0] = 1
    while pq:
        curSum, curRow, curCol = heapq.heappop(pq)
        if curRow == N-1 and curCol == N-1:
            if curSum < minSum:
                minSum = curSum
        for r_d, c_d in dir:
            nextRow, nextCol = curRow+r_d, curCol+c_d
            if nextRow < 0 or nextCol < 0:
                continue
            if nextRow >= N or nextCol >= N:
                continue
            if visit[nextRow][nextCol] == 1:
                continue
            visit[nextRow][nextCol] = 1
            heapq.heappush(
                pq, (curSum+uMap[nextRow][nextCol], nextRow, nextCol))


Solve()
print(minSum)
