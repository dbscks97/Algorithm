from itertools import permutations
def solution(numbers):
    answer = 0
    result=[]
    ans=[]
    
    for k in range(1, len(numbers)+1):
        permutations_list = list(permutations(numbers, k))
        for perm in permutations_list:
            combined_num = int(''.join(map(str, perm)))
            result.append(combined_num)

    for i in result:
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i>=2 and i not in ans:    
            ans.append(i)
        

    answer = len(ans)
    return answer