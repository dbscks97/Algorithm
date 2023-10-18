def solution(progresses, speeds):
    answer = []  # 결과를 저장할 리스트
    days_left = []  # 각 작업의 완료까지 남은 일자를 저장할 리스트
    
    # 각 작업의 완료까지 남은 일자를 계산하여 days_left 리스트에 저장
    for progress, speed in zip(progresses, speeds):
        days = (100 - progress) // speed
        if (100 - progress) % speed != 0:
            days += 1
        days_left.append(days)
    
    # 각 배포마다 몇 개의 작업이 완료되는지 계산
    count = 1
    max_days = days_left[0]
    for i in range(1, len(days_left)):
        if days_left[i] <= max_days:
            count += 1
        else:
            answer.append(count)
            max_days = days_left[i]
            count = 1
    
    answer.append(count)  # 마지막 배포에 대한 결과 추가
    
    return answer
