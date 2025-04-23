total = int(input())
num = int(input())
res = 0
for i in range(num):
  price, count = map(int, input().split())
  res += price*count
if total == res:
  print('Yes')
else:
  print('No')