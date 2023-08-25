from collections import deque
def solution(people, limit):
    answer = 0
    result = 0
    sort=sorted(people,reverse=True)
    q=deque()
    
    for i in sort:
        q.append(i)

    for cur in sort:
        if q:
            if cur + q[-1] <=limit:
                if len(q)>1:
                    a = q[-1]
                    q.popleft()
                    q.pop()
                    answer+=1
                else:
                    q.pop()
                    answer+=1
            else:
                q.popleft()
                answer+=1
            
    return answer