"""
* Problem   : 1699
* Title     : 제곱수의 합
* Link      : https://www.acmicpc.net/problem/1699
* Category  : Dynamic Programming
"""

# python3로 하면 시간초과지만
# 우리의 pypy3는 저를 실망시키지 않는군요

n = int(input())
sqrt_n = int(n ** 0.5)

dp = [100001] * 1000001
dp[0] = 0

for i in range(1, n+1):
    for j in range(1, sqrt_n + 1):
        dp[i] = min(dp[i], dp[i-j**2] + 1)

print(dp[n])

# 이 문제는 그리디 하게 풀면 안되는걸까?
# 사례 : n = 12
# greedy solution -> 12 = 3^2 + 1^2 + 1^2 + 1^2 (4개)
# real solution -> 12 = 2^2 + 2^2 + 2^2 (3개)
