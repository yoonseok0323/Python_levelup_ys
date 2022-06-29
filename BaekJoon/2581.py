#2581 소수
a = int(input())
b = int(input())
num = []

for i in range(a,b+1):
  if i == 1:
    pass
  elif i == 2:
    num.append(i)
  else:
    for c in range(2,i):
      inte =0
      if i % c ==0:
        inte = 1
        break
    if inte == 0:
        num.append(i)
if len(num)==0:
  print(-1)
else:               
  print(sum(num))
  print(min(num))
