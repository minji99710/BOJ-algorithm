a=b=c=1
while True:
  sum=0
  lst = []
  a,b,c = map(int, input().split())
  lst.extend([a, b, c])
  long = lst.pop(lst.index(max(a,b,c)))
  for i in lst:
    sum += i**2

  if a==0 and b==0 and c==0:
    break

  print("right") if long**2==sum else print("wrong")