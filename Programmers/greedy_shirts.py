def solution(n, lost, reserve):
    answer = 0
    
    student =[]
    for i in range(1,n+1):
        student.append(i)
    
    have = list(set(student)-set(lost))
    cnt = 0
    
    for j in lost:
        if (j-1) in reserve:
            lost.remove(j)
            cnt +=1
        elif (j+1) in reserve:
            lost.remove(j)
            cnt +=1
                
    answer = int(len(have))+cnt
    
    
    
    
    return answer


# 30% 아직 미완

