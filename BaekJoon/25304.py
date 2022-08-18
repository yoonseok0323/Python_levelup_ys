#25304
price = int(input())
stuff = int(input())
all=[]
for i in range(stuff):
  a,b= map(int,input().split())
  c = a*b
  all.append(c)
if sum(all) == price :
  print("Yes")
else:
  print("No")
