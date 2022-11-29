import sys


def input_data():
    readl = sys.stdin.readline
    return [list(map(int, readl().split())) for _ in range(9)]



sudoku = input_data()

emptyArr = []

def DFS(level):
  if level==len(emptyArr):
    for i in sudoku:
      print(*i)
    return
  curRow,curCol = emptyArr[level]
  for i in range(1,10):
    sudoku[curRow][curCol]=i
    if Check(curRow,curCol):
      DFS(level+1)

def Check(row,col):
  checkDict = dict()
  for i in range(10):
    checkDict[i] = 0
  for i in range(9):
    curNum = sudoku[i][col]
    if curNum!=0 and checkDict[curNum]==1:
      return False
    checkDict[curNum]+=1
  
  for i in range(10):
    checkDict[i] = 0
  
  for i in range(9):
    curNum = sudoku[row][i]
    if curNum!=0 and checkDict[curNum]==1:
      return False
    checkDict[curNum]+=1

  for i in range(10):
    checkDict[i] = 0

  if 0<=row<=2 and 0<=col<=2:
    for i in range(0,3):
      for j in range(0,3):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 0<=row<=2 and 3<=col<=5:
    for i in range(0,3):
      for j in range(3,6):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 0<=row<=2 and 6<=col<=8:
    for i in range(0,3):
      for j in range(6,9):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 3<=row<=5 and 0<=col<=2:
    for i in range(3,6):
      for j in range(0,3):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 3<=row<=5 and 3<=col<=5:
    for i in range(3,5):
      for j in range(3,5):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 3<=row<=5 and 6<=col<=8:
    for i in range(3,6):
      for j in range(6,9):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 6<=row<=8 and 0<=col<=2:
    for i in range(6,9):
      for j in range(0,3):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 6<=row<=8 and 3<=col<=5:
    for i in range(6,9):
      for j in range(3,6):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  elif 6<=row<=8 and 6<=col<=8:
    for i in range(6,9):
      for j in range(6,9):
        curNum = sudoku[i][j]
        if curNum!=0 and checkDict[curNum]==1:
          return False
        checkDict[curNum]+=1
  return True

def Solve():
  for i in range(9):
    for j in range(9):
      if sudoku[i][j]==0:
        emptyArr.append((i,j))
  DFS(0)


Solve()