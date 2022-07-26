#2501
N,K = map(int,input().split())
num=[]

for i in range(1,N+1):
  if N%i == 0:
    K -=1
    if K==0:
      result=i
      break
# k번째로 작은 수를 출력한다는 말
# ex) 6의 약수 중 3번째로 작은 수를 출력할 때. i가 6의 약수에 해당될때마다 k-1를 하므로써 사실상 카운트를 진행.
# 그러므로 3번째를 출력하기 위해서는 3번째 약수에 해당 된다는 말이되고, 이는 k값이 0이 된다는 것을 의미한다.

if K>0:
  print(0)
else:
  print(result)