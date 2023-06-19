def solution(n, lost, reserve):
    answer = 0
    cnt=0
    lost.sort()
    reserve.sort()
   
    
    lost_to_remove = []
    reserve_to_remove = []

    for i in lost:
        if i in reserve:
            lost_to_remove.append(i)
            reserve_to_remove.append(i)

    for i in lost_to_remove:
        lost.remove(i)

    for i in reserve_to_remove:
        reserve.remove(i)
            
    num = len(lost)       
    
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            a = lost[i]
            reserve.pop(reserve.index(a-1))
            cnt+=1
        elif lost[i]+1 in reserve:
            a = lost[i]
            reserve.pop(reserve.index(a+1))
            cnt+=1
        
    answer = n - num +cnt
    return answer