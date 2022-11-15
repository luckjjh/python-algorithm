import sys
# 부동산으로 엄청난 돈을 번 철희는 전 세계적으로 유명한 랜드마크가 될 만한 빌딩을 
# 지으려고 한다. 무려 999,999,999 층짜리 건물이다.

# 미신을 광신하는 철희는 투자할 때 마다 4와 관련된 숫자가 들어간 투자는 백프로 
# 손해를 봤다. 그래서 이 빌딩에는 4가 전혀 들어가지 않게 하려고 한다. 
# 그래서 4층은 5층이라고 표시하고 14층은 16층으로 표시를 하였다. 이렇게 모든 자리에 4가 들어가면 빼고 다음 숫자로 대체를 하였다.

# 드디어 빌딩은 완공이 되고 사람들이 입주를 하였는데, 입주자들은 실제 자기가 입주한 
# 층이 몇 층인지 궁금해졌다. 이 빌딩의 층 수 N(1≤N≤999,999,999)이 주어지면 실제 층 
# 수를 구해주는 프로그램을 작성하시오.

def Input_data():
    readl = sys.stdin.readline
    N = int(input())
    return N

sol = 0
N = Input_data() 


def Solve():
  digit = [n if n<4 else n-1 for n in map(int,str(N))]
  sum = 0
  for i in digit:
    sum = sum*9+i
  print(sum)


Solve()