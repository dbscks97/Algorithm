def solution(answers):
    answer = []
    ans = []
    one=[1,2,3,4,5] * int(10000//5)
    two=[2,1,2,3,2,4,2,5] * int(10000//8)
    three=[3,3,1,1,2,2,4,4,5,5] * int(10000/10)
    one_count=0
    two_count=0
    three_count=0
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            one_count+=1
            
        if answers[i] == two[i]:
            two_count+=1
            
        if answers[i] == three[i]:
            three_count+=1
    ans.append(one_count)
    ans.append(two_count)
    ans.append(three_count)
    max_ans = max(ans)
    
    for i in range(len(ans)):
        if ans[i] == max_ans:
            answer.append(i+1)
        
    return answer