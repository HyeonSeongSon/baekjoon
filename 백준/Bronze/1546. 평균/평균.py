n = int(input())
s = list(map(int, input().split()))
print(round(sum(s)/max(s)*100/n,2))