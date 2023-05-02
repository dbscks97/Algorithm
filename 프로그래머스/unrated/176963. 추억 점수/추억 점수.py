def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        total = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                a =name.index(photo[i][j])
                total += yearning[a]
        answer.append(total)    
    
    return answer

if __name__=='__main__':
    name = list(map(str,s.readline().split()))
    yearning = list(map(int,s.readline().split()))
    photo = [list(map(str,s.readline().split()))]
    
    solution(name,yearning,photo)