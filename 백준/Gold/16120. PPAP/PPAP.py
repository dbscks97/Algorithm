from sys import stdin as s
#s = open('input.txt','rt')
arr = input()


stack = []


for i in range(len(arr)):
    stack.append(arr[i])
    if stack[-4:] == ['P','P','A','P']:
        for j in range(1,4):
            stack.pop()
    
if stack==['P'] or stack ==['P','P','A','P']:
    print('PPAP')
else:
    print('NP')
        


