def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    
    for i in range(len(number)):
        if cnt == k:
            break
        
        if not stack and number:
            stack.append(number[i])
            continue
        
        if stack:
            while(stack and stack[-1] < number[i] and cnt<k):
                    stack.pop()
                    cnt+=1
            stack.append(number[i])
            
    if len(stack) == len(number):
        for i in range(k):
            stack.pop()
            
    if len(stack) != len(number)-k:
        stack.append(number[i:])
    
            
    b = "".join(stack)
    answer=b
    return answer