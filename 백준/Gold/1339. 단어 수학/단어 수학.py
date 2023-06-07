from sys import stdin as s
from collections import deque

n = int(s.readline())
words = []
alpha_value = {}
for _ in range(n):
    words.append(list(s.readline().rstrip()))

for word in words:
    for i in range(len(word)):
        if word[i] not in alpha_value:
            alpha_value[word[i]] = 10 ** (len(word) - 1 - i)
        
        else:
            alpha_value[word[i]] += 10 ** (len(word) - 1 - i)

alpha_value = sorted(alpha_value.items(), key=lambda x: x[1], reverse=True)

alpha_to_num = {}

num=9
for alpha in alpha_value:
    alpha_to_num[alpha[0]] = num
    num -= 1

result=0
for word in words:
    for i in range(len(word)):
        if word[i] in alpha_to_num:
            number = alpha_to_num[word[i]]
            result += (10 **(len(word)-1-i))* number
    
print(result)