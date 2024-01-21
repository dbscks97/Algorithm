def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
    else:
        min_arr = min(arr)
        for i in arr:
            if i != min_arr:
                answer.append(i)
                
    return answer

