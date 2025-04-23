N, X = map(int, input().split())
A = list(map(int, input().split()))
res = [x for x in A if x < X]
res_str = list(map(str, res))
print(' '.join(res_str))