from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    q = deque()
    for i in range(len(goal)):
        a = goal[i]
        q.append(a)
        
    index_a = 0
    index_b = 0
    
    for j in range(len(goal)):
        b = q.popleft()
        
        if index_a < len(cards1) and b == cards1[index_a]:
            index_a += 1
            continue

        elif index_b < len(cards2) and b == cards2[index_b]:
            index_b += 1
            continue
        else:
            break
        
        
    if (index_a + index_b) == len(goal):
        answer = "Yes"
    else:
        answer = 'No'
        
    return answer