s = [i for i in range(1,31)]
for i in range(28):
  a = int(input())
  s.remove(a)
print(' '.join(list(map(str, s))))