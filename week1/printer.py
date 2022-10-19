from cgi import test
import sys
from collections import deque

# 컴퓨터 과학과 학생회의 유일한 프린터는 매우 무거운 작업량을 겪고 있다.
# 때로는 수백 개의 작업으로 인해 한 페이지 출력을 얻으려면 몇 시간을 기다려야 할 수 있다.
# 일부 작업이 다른 작업보다 중요하기 때문에 학생회의 회장인 철수는 대기 열에 대한 간단한 우선 순위 시스템을 발명하고 구현했다.
# 이제 각 작업에 우선 순위가 1과 9 사이(9가 가장 높은 우선 순위이고 1이 가장 낮음)에서 지정된다.

# 프린터는 다음과 같이 작동한다.

# - 대기 열의 첫 번째 작업인 J를 대기 열에서 가져옴.
# - 대기 열에 작업 J보다 우선 순위가 높은 작업이 있는 경우, J를 인쇄하지 않고 대기 열 끝으로 이동 시킴.
# - 그렇지 않으면 작업 J를 인쇄 함 (다시 대기 열에 넣지 않음)

# 이러한 방식의 발명으로 우선순위가 높은 중요한 문서는 매우 빨리 인쇄되지만, 중요도가 낮은 다른 문서들은 인쇄되기까지 꽤 오래 기다려야 할 수 도 있다.

# 위 방법으로 프린터가 작동할 때, 현재 대기 열에 있는 문서의 수와 우선순위가 주어졌을 때, 어떤 한 문서가 몇 번째 순서로 인쇄되는지 출력하는 프로그램을 작성하자.


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    pList = list(map(int, readl().split()))
    return N, M, pList


testCase = int(sys.stdin.readline())

for _ in range(testCase):
    cnt = 0
    N, M, pList = Input_Data()
    q = deque(enumerate(pList))
    while q:
        check = True
        curDoc = q.popleft()
        for item in q:
            if item[1] > curDoc[1]:
                q.append(curDoc)
                check = False
                break
        if check:
            cnt += 1
            if curDoc[0] == M:
                print(cnt)
                break
        else:
            continue
