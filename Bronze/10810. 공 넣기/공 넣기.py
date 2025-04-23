a, b = map(int, input().split())
m=[]
m+= [0]*a
for _ in range(b):
   i,j,k = map(int, input().split())
   m[i-1:j] = [k]*(j-i+1)   
print(' '.join(list(map(str, m))))