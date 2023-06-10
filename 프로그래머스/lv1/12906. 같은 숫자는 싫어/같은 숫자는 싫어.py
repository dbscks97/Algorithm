def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        
        if answer:
            a=answer.pop()
            if a==arr[i]:
                answer.append(a)
            else:
                answer.append(a)
                answer.append(arr[i])
    return answer