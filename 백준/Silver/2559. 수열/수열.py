from sys import stdin as s

N, K = map(int, s.readline().split())

arr = list(map(int, s.readline().split()))

# 누적합 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

result = -10000000
for i in range(N - K + 1):
    # 슬라이딩 윈도우를 이용해 구간 합 계산
    window_sum = prefix_sum[i + K] - prefix_sum[i]
    result = max(result, window_sum)

print(result)
