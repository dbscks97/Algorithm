# 정수를 문자열로 바꾸는 함수 str(i) , 자리수별로 판별하기위해 문자열로 바꿈
n = int(input())
hansu = 0

for i in range(1,n+1):
    if i < 100:
        hansu += 1
    else :
        nums = list(map(int,str(i)))
        if nums[0] - nums[1] == nums[1] -nums[2]:
            hansu += 1
print(hansu)