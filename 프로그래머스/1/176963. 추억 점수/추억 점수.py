def solution(name, yearning, photo):
    answer = []
    x = len(photo)
    for i in range(x):
        y = len(photo[i])
        count = 0
        for j in range(y):
            for z in range(len(name)):
                if photo[i][j] == name[z]:
                    count += yearning[z]
        answer.append(count)
    return answer