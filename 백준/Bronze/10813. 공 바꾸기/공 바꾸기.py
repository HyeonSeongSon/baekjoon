a, b = map(int, input().split())
m=[i for i in range(1,a+1)]
for _ in range(b):
  i,j = map(int, input().split())
  if i != j:
     x = m[i-1]
     y = m[j-1]
     m[i-1] = y
     m[j-1] = x
print(' '.join(list(map(str, m))))