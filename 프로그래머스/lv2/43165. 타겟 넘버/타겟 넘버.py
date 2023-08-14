from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    length = len(numbers)
    
    q.append((-1 * numbers[0],0))
    q.append((numbers[0],0))
    
    while q:
        cq,cindex = q.popleft()
        cindex +=1
        if cindex < length:
            q.append((cq + numbers[cindex], cindex))
            q.append((cq + (-1 * numbers[cindex]), cindex))
        else:
            if target == cq:
                answer+=1
            
    

    return answer