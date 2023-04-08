n = int(input())

for i in range(n):
    num, word = input().split()
    
    for j in word:
        print(j * int(num), end='')
    print()