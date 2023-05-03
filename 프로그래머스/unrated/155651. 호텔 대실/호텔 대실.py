from sys import stdin as s
def solution(book_time):
    result=[]
    ans=[]
    answer=0
    
    for i in range(len(book_time)):
        hour,minute = book_time[i][0].split(':')
        end_hour,end_minute = book_time[i][1].split(':')
        hour = int(hour) * 60
        end_hour = int(end_hour) * 60
        end = end_hour + int(end_minute)
        start = hour + int(minute)
        result.append((start,end))
        result.sort()   

    ans.append(result[0])
    for i in range(1,len(result)):
        ans.append(result[i])
        for j in range(len(ans)):
            if result[i][0]-10 >= ans[j][1]:
                ans.remove(ans[j])
                break
    answer=(len(ans))
    
    
    return answer