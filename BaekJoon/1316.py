n = int(input())
num = n
for i in range(n):
  word = input()               
  for a in range(len(word)-1): #if word aabbcc
    if word[a] != word[a+1]: # a=1 word[1]=a, word[2]=b
      dif = word[a+1:]       # dif = bbcc
      if word[a] in dif:     # a in bbcc 일 경우 -1 BUT bbcc안에 a가 없으므로 해당 되지 않음.
        num -= 1
        break
print(num)
