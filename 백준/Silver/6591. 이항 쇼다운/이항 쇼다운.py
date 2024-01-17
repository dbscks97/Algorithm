from sys import stdin as s

def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1

    k = min(k, n - k)
    result = 1
    for i in range(k):
        result *= n - i
        result //= i + 1

    return result

while True:
    n, k = map(int, s.readline().split())
    if n == 0 and k == 0:
        break

    result = binomial_coefficient(n, k)
    print(result)
