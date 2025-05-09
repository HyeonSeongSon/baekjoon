import sys
hard = []
res = []
for _ in range(5):
  ram = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  inputs = sys.stdin.readline().strip()
  for i in range(len(inputs)):
    ram[i] = inputs[i]
  hard.append(ram)
for j in range(15):
  for i in range(5):
    if hard[i][j] == ' ':
      pass
    else:
      res.append(hard[i][j])
print(''.join(res))