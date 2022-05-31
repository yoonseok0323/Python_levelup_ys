n = int(input())
num = list( map(int,input().split()) )
cnt = 0
for i in num:
  inteager =0
  if i > 1:             # i == each num
    for a in range(2,i):
      if i % a==0:    # 대입값(i)를 2~(i-1)의 값으로 나누었을 때 나머지가 0이 되는 경우는 소수가 아님
        inteager = 1 
        break
    if inteager == 0 : # 위의 조건문을 모두 통과하여 내려온 경우는 소수.
      cnt +=1
print(cnt)


