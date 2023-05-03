def solution(targets):
    answer = 1
    targets.sort(key=lambda x:x[1])
    h = targets[0][1]
    for i in range(1,len(targets)):
        if h > targets[i][0]:
            continue
        else:
            h = targets[i][1]
            answer+=1
    return answer