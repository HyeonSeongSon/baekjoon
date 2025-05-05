ca = ['c=','c-','d-','lj','nj','s=','z=', 'dz=']
text = input()
count = 0
while text:
  matched = False
  for a in ca:
    if text[:len(a)] == a:
      count +=1
      text = text[len(a):]
      matched = True
      break
  
  if not matched:
    text = text[1:]
    count +=1
print(count)