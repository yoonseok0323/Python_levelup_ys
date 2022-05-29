#10872 팩토리얼

a = int(input())
num = 1
for i in range(1,a+1):
  if a==0:
    print(num)
  else:
    num*=i
print(num)
