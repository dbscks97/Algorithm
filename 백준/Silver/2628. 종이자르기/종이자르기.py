x,y = map(int,input().split())

x_list = [0,x]
y_list = [0,y]

for _ in range(int(input())):
    a,b = map(int,input().split())
    
    if a == 0:
        y_list.append(b)
    elif a ==1:    
        x_list.append(b)

x_list.sort()
y_list.sort()

result =0 

for i in range(len(x_list)-1):
    for j in range(len(y_list)-1):
        width = x_list[i+1]-x_list[i]
        height = y_list[j+1]-y_list[j]
        
        result = max(result, width*height)
print(result)
        