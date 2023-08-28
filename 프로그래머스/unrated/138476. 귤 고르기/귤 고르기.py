def solution(k, tangerine):
    answer = 0
    cnt = 0
    dict ={}
    for num in tangerine:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    
    for num in sorted_dict:
        c =num[1]
        if c>k:
            answer+=1
            break
        
        if cnt >=k:
            break
        cnt += num[1]
        answer+=1
    return answer