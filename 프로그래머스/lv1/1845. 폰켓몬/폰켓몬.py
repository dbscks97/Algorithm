def solution(nums):
    answer = 0
    arr=set(nums)
    choice = len(nums)//2
    if len(arr)>=choice:
        answer=choice
    else:
        answer=len(arr)
    return answer