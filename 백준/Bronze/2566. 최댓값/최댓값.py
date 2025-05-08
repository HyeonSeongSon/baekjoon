import sys

X = []
for i in range(9):  
    data = list(map(int, sys.stdin.readline().strip().split()))
    X.append(data)

max_value = [0,0,0]
for i in range(9):
  for j in range(9):
    if X[i][j] > max_value[0]:
      max_value = [X[i][j], i, j]
print(max_value[0])
print(max_value[1]+1, max_value[2]+1)