#1546
subject = int(input())
new_grade = []
grade =  list(map(int,input().split()))
max_grade = max(grade)

for i in grade:
  r = i/max_grade*100
  new_grade.append(r)
result = sum(new_grade)/subject
print(result)
