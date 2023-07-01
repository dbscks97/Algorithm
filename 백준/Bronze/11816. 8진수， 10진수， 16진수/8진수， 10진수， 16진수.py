from sys import stdin as s

X = list(map(str,s.readline().strip()))
result = 0
length = len(X)

for i in range(len(X)):
    if X[0] == '0':
        if X[1] =='x':
            if X[i] =='a':
                result += 10 * (16 **(length-i-1))
            elif X[i] =='b':
                result += 11 * (16 **(length-i-1))
            elif X[i] =='c':
                result += 12 * (16 **(length-i-1))
            elif X[i] =='d':
                result += 13 * (16 **(length-i-1))
            elif X[i] =='e':
                result += 14 * (16 **(length-i-1))
            elif X[i] =='f':
                result += 15 * (16 **(length-i-1))
            elif X[i] =='x':
                continue
            else:
                result += int(X[i]) * (16 **(length-i-1))
        else:
            result += int(X[i]) * (8 **(length-i-1))
    else:
        result += int(X[i]) * (10 **(length-i-1))
    
print(result) 
