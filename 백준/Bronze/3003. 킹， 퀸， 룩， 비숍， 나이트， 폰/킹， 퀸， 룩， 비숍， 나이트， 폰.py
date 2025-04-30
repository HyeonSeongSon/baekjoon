a = list(map(int, input().split()))
t = [1,1,2,2,2,8]
for i in range(6):
    t[i] = str(t[i] - a[i])
print(' '.join(t))