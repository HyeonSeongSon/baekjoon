import sys
input = sys.stdin.readline
cnt = int(input())
words = [input().strip() for i in range(cnt)]
words = list(set(words))
words = sorted(words, key=lambda x: (len(x), x))
print(*words, sep='\n')