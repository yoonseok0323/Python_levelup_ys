#17608 ,막대
'''
가장 마지막에 들어간 막대를 기준으로 크면 +1이 되고 커진 수가 기준으로 바뀐다는 로직으로 구성 
실행결과 시간초과 결과가 나온다
for문을 돌려서 그런 것으로 보인다.
'''
n = int(input())
stack = [ ]
sum = 1

for i in range(n):
  i = int(input())
  stack.append(i)

standard = stack[-1]

for j in range(n):
  change = stack.pop()
  if change <= standard:
    pass
  elif change > standard:
    standard = change
    sum +=1
print(sum)
