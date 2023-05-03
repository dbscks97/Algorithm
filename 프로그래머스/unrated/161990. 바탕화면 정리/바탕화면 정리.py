from sys import stdin as s

def solution(wallpaper):
    answer=[50,50,0,0]
    for i in range(len(wallpaper)):
        for j  in range(len(wallpaper[i])):
            if wallpaper[i][j] =='#':
                    answer[0]=min(answer[0],i)
                    answer[1]=min(answer[1],j)
                    answer[2]=max(answer[2],i)
                    answer[3]=max(answer[3],j)
    answer[2]+=1
    answer[3]+=1
    return answer  

if __name__=='__main__':
    
    wallpaper = [list(map(str,s.readline().strip()))for _ in range(5)]
    ans = solution(wallpaper)

    print(ans)
    
    