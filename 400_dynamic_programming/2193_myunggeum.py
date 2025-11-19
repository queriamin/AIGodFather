"""
* Problem   : 2193
* Title     : 이친수
* Link      : https://www.acmicpc.net/problem/2193
* Category  : Dynamic Programming
"""
n = int(input())

dp = [1 for _ in range(100)]

dp[1] = 1
dp[2] = 1
dp[3] = 2

if n > 3:
    for i in range(4,n+1):
        for j in range(2,i):
            dp[i] += dp[i-j]

print(dp[n])
