def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue
        
        if stack:
            if s[i] ==')':
                if stack[-1] =='(':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

    if stack:
        answer=False
    
    
    return answer