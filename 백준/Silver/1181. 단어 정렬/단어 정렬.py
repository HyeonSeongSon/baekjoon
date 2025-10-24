cnt = int(input())
words = [input() for i in range(cnt)]
words = list(set(words))
words = sorted(words, key=lambda x: (len(x), x))
print(*words, sep='\n')