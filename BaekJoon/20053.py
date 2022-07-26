# 200053
T=int(input())

for i in range(T):
    N = int(input())
    num=list(map(int,input().split()))
    print(min(num),max(num))