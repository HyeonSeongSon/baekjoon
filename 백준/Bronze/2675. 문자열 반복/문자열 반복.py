n = int(input())
for i in range(n):
    x,y = input().split()
    w = [a*int(x) for a in y]
    print(''.join(w))