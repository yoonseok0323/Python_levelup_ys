#1929 소수
a,b = map(int,input().split())
num = []
sosu = []
for i in range(a,b+1):
  if i == 1:
    pass
  elif i == 2:
    sosu.append(i)
  else:
    for c in range(2,i):
      inte =0
      if i % c ==0:
        inte = 1
        break
    if inte == 0:
      sosu.append(i)
print(sosu)
