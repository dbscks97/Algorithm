import sys

read = sys.stdin.readline
num = int(read())
for i in range(num):
    num_list = list(map(int,read().split()))
    avg = sum(num_list[1:]) / num_list[0]
    
    cnt = 0
    for score in num_list[1:]:
        if score> avg:
            cnt +=1
    print(f'{cnt/num_list[0]*100:.3f}%')