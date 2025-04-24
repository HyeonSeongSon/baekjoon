n = int(input())
w = input()
res = [w[i] for i in range(n)]
print(sum(list(map(int, res))))