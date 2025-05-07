n = int(input())
counts = n
for i in range(n):
  text = input()
  alphabet_list = []
  for idx, a in enumerate(text):
    if idx < len(text) - 1 and text[idx] == text[idx+1]:
      pass
    elif a not in alphabet_list:
      alphabet_list.append(a)
    elif a in alphabet_list:
      counts -= 1
      break
print(counts)