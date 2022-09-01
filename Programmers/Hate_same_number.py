def solution(arr):
    answer = []
    for i, j in enumerate(arr):
        try:
            if j != arr[i+1]:
                answer.append(j)
        except IndexError:
            answer.append(j)

    return answer


# 1 1 3 3 0 1 1
# 0 1 2 3 4 5 6

# 1 != 1

