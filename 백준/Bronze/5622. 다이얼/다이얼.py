d = list(input().lower())
s = 0
for i in d:
  if (i == 'a') or (i == 'b') or (i == 'c'):
    s += 3
  elif (i == 'd') or (i == 'e') or (i == 'f'):
    s += 4
  elif (i == 'g') or (i == 'h') or (i == 'i'):
    s += 5
  elif (i == 'j') or (i == 'k') or (i == 'l'):
    s += 6
  elif (i == 'm') or (i == 'n') or (i == 'o'):
    s += 7
  elif (i == 'p') or (i == 'q') or (i == 'r') or (i == 's'):
    s += 8
  elif (i == 't') or (i == 'u') or (i == 'v'):
    s += 9
  elif (i == 'w') or (i == 'x') or (i == 'y') or (i == 'z'):
    s += 10
print(s)