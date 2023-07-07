from sys import stdin as s

K, N = map(int,s.readline().split())
lan = []
for i in range(K):
    a = int(s.readline())
    lan.append(a)

start = 1
end = max(lan)


while(start<=end):
    mid = (start+end) // 2
    length=0
    
    for i in range(len(lan)):
        length += (lan[i] // mid)
    
    if length >= N :
        start = mid +1
    else:
        end = mid -1


print(end)
        
