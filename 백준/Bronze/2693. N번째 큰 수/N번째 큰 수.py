t = int(input())

for _ in range(t):
  num = list(map(int, input().split()))
  num.sort(reverse=True)
  print(num[2])