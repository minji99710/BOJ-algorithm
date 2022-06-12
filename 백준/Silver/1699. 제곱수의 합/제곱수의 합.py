import sys
n = int(sys.stdin.readline())

d=[0]*(n+1)

for i in range(1, n+1):
  d[i]=i
  for j in range(1, int(i**0.5)+1):
    d[i] = min(d[i], d[i-j**2]+1)

print(d[n])
  