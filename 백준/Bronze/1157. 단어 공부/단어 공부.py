from collections import Counter
c = Counter(list(input().upper())).most_common(2)
if len(c) > 1 and c[0][1] == c[1][1]:
  print('?')
else:
  print(c[0][0])