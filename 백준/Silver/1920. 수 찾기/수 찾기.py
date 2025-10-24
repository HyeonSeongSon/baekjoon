import sys
input = sys.stdin.readline

a = int(input())
num1 = set(map(int, input().strip().split()))
b = int(input())
num2 = list(map(int, input().strip().split()))

for n in num2:
  print(1 if n in num1 else 0)