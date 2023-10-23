from sys import stdin as s
while True:
    arr = list(map(str,s.readline().rstrip()))
    stack = []
    if arr[0] == '.':
        break
    count = 0
    for i in range(len(arr)):
       if arr[i] == '[':
           stack.append(arr[i])
       elif arr[i] == '(':
           stack.append(arr[i])
       elif arr[i] == ']':
           if stack:
            if stack.pop() == '[':
                continue
            else:
                count += 1
                break
           else:
               count += 1
       elif arr[i] == ')':
           if stack:
            if stack.pop() =='(':
                continue
            else: 
                count += 1
                break
           else:
               count += 1
       else:
           continue
    
    if count != 0:
        print('no')
    else:
        if stack:
            print('no')
        else:
            print('yes')
    