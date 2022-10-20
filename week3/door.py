import sys
# n개의 같은 크기의 벽장들이 일렬로 붙어져 있고 벽장의 문은 n-2개만이 있다.
# 한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면) 그 벽장 앞으로 움직일 수 있다.

# 그림은 7개의 벽장의 예이다. 그림에서 2번 벽장과 5번 벽장이 열려있고, 나머지 벽장은 닫혀 있다.
# 벽장 문은 좌우 어느 쪽이든 그 이웃 벽장이 열려 있다면 그 쪽으로 한 칸씩 이동할 수 있다.
# 그림에서 주어진 상태에서는 1번 벽장을 닫고 있는 벽장문을 오른쪽으로 한 칸 이동함으로써 1번 벽장을 사용할 수 있다.
# 이때 2번 벽장은 닫혀져 사용할 수 없다. 역시 5번 벽장이 열려 있으므로 4번 벽장 또는 6번 벽장 앞의 벽장문을 5번 벽장 앞으로 이동시킬 수 있다.


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    open1, open2 = map(int, readl().split())
    M = int(readl())
    dList = [int(readl()) for _ in range(M)]
    return N, open1, open2, M, dList


N, open1, open2, M, dList = Input_Data()

minMove = 987654321


def Solve(idx, left, right, cnt):
    global minMove
    if idx == M:
        minMove = min(cnt, minMove)
        return
    if minMove <= cnt:
        return

    if dList[idx] > left:
        Solve(idx+1, left, dList[idx], cnt+abs(right-dList[idx]))
    if dList[idx] < right:
        Solve(idx+1, dList[idx], right, cnt+abs(left-dList[idx]))


Solve(0, min(open1, open2), max(open1, open2), 0)
print(minMove)
