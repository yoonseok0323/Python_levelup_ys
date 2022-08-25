# 가장 빈도수가 높은 인덱스에 접근하는 방법에 대해서 시간이 오래걸린 문제

string = input().lower()
new_string = list(set(string)) # misp
cnt = []

for i in new_string:
  count = string.count(i) #misp에 해당하는 요소의 개수를 센다
  cnt.append(count)       # 카운트한 개수를 cnt리스트에 추가한다.
#print(cnt)

if cnt.count(max(cnt)) > 1 : # 만약 cnt max값의 개수가 1개보다 많을 떄
  print("?")
else:
  print(new_string[cnt.index(max(cnt))].upper())
