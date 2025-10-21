import sys

n = int(input())
l = list(map(int, input().split()))

l.sort()

res = 0
m = 0
for i in l:
  m = m + i
  res += m
print(res)