import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
  data.append(list(map(int, sys.stdin.readline().split())))
  
data.sort(key=lambda x: (x[0], x[1]))


for x,y in data:
  print(x,y)