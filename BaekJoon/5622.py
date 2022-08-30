#5622
word = input()
alpha = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
sum=0

for i in word: #W한번 루프 A한번 루프
    for j in alpha: 
        if i in j: #j에 i가있으면 index 추출
          sum+= alpha.index(j)+3 
          #print(alpha.index(j))
print(sum)
