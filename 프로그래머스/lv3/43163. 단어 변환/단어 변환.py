from collections import deque
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    
    q=deque()
    q.append((begin,0))
    while q:
        b,idx = q.popleft()
        v = [0]*len(words)
        
        if b == target:
            break
        for i in range(len(words)):
            count = 0 
            for j in range(len(words[i])):
                if b[j] == words[i][j]:
                    count += 1
                    v[i] = count
        
        for k in range(len(v)):
            if v[k] == len(words[i])-1:
                q.append((words[k],idx+1))
                words[k] = str(idx)

    return idx