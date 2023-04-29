# 백준 - 8958번
# for j in a: 는 a의 값을 j에 하나씩 대입하여 돌린다.
# sys.stdin.readline().strip() 의 strip()은  읽어들인 무자열에서 양쪽 끝에 있는 공백과 개행문자를 모두 제거한다.


# n = int(input())

# for i in range(n):
#     a = input()
#     sum=0
#     cnt=0
    
#     for j in a:
#         if j == 'O':
            
#             cnt += 1
#             sum += cnt
#         else:
#             cnt = 0
#     print(sum)

import sys
n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline().strip()
    sum=0
    cnt=0
    
    for j in a:
        if j == 'O':
            
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)