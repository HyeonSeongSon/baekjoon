import io
import os
import sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

def main():
  cnt = [0]*2000001
  offset = 1000000

  for _ in range(int(input())):
    cnt[int(input()) + offset] = 1

  print('\n'.join(map(str, (i - offset for i in range(2000001) if cnt[i]))))

if __name__ == '__main__':
    main()