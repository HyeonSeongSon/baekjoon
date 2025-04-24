a = [-1]*26
for idx, m in enumerate([i for i in input()]):
  if a[ord(m)-97] == -1:
    a[ord(m)-97] = idx
print(' '.join(list(map(str, a))))