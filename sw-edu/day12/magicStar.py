import sys

def input_data():
    readl = sys.stdin.readline
    map_star = [list(readl().strip()) for _ in range(5)]
    return map_star

map_star = input_data()

alphaDict = {
  'A':1,
  'B':2,
  'C':3,
  'D':4,
  'E':5,
  'F':6,
  'G':7,
  'H':8,
  'I':9,
  'J':10,
  'K':11,
  'L':12
}

def check():
    magic = [(0, 2, 5, 7), (7, 8, 9, 10), (10, 6, 3, 0), (1, 2, 3, 4,), (4, 6, 9, 11), (11, 8, 5, 1)]
    
    for m in magic:
        cnt = 0
        for i in range(4):
            x, y = magic_index[m[i]]
            if magic_star[x][y] == 0: break

            cnt += magic_star[x][y]
            if i == 3 and cnt != 26: return False

    return True

def dfs(level):
    if not check(): return
    if level == 12:
        for i in range(5):
            temp = []
            for j in range(9):
                if magic_star[i][j] == -1: temp.append('.')
                else: temp.append(chr(magic_star[i][j] + 64))
            print(''.join(temp))
        exit()
        return
    
    if magic_visit[level]:
        dfs(level + 1)
        return

    for i in range(12):
        if num_visit[i]: continue

        x, y = magic_index[level]
        
        magic_star[x][y] = i + 1
        num_visit[i] = 1

        dfs(level + 1)

        magic_star[x][y] = 0
        num_visit[i] = 0
        
    
magic_index = [(0, 4),
              (1, 1), (1, 3), (1, 5), (1, 7),
              (2, 2), (2, 6),
              (3, 1), (3, 3), (3, 5), (3, 7),
              (4, 4)]
magic_visit = [0] * 12
num_visit = [0] * 12

magic_star = []

for i in range(5):
    temp = []
    for j in range(9):
        if map_star[i][j] == '.': temp.append(-1)
        elif map_star[i][j] == 'x': temp.append(0)
        else:
            num = ord(map_star[i][j]) - 64
            temp.append(num)
            num_visit[num-1] = 1
            for k in range(12):
                if magic_index[k] == (i, j): magic_visit[k] = 1

    magic_star.append(temp)

dfs(0)
