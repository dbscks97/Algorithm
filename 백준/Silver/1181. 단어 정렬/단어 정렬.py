# 빈 리스트를 만들고 입력한 단어들을 차례로 append한다. 주의할 점은 sys.stdin.readlin()은 개행도 포함하므로 strip()으로 없애준다.
# set() 함수를 사용해서 중복된 값을 제거한다.
# sort(key=len)을 사용하여 문자가 짧은 순으로 정렬한다.
# for i in nums: 를 사용하여 nums에 들어있는 데이터를 반복문을 통해 출력.

import sys

n = int(sys.stdin.readline())
nums = []

for i in range(n):
    nums.append(sys.stdin.readline().strip())

set_lst = set(nums)
nums = list(set_lst)
nums.sort()
nums.sort(key=len)

for i in nums:
    print(i)
    
    