"""
* Problem   : 2225
* Title     : 합분해
* Link      : https://www.acmicpc.net/problem/2225
* Category  : Dynamic Programming
"""
n, k = [int(x) for x in input().split()]
MOD = int(1e9)

# dp[n][k] : 0~n까지의 정수를 k개 더해서 합이 n이 되는 경우의 수
dp = [[0] * 201 for _ in range(201)]

# n = 0 -> dp[0][k] = 1
# n = 1 -> dp[1][k] = k
for i in range(k+1):
    dp[0][i] = 1
    dp[1][i] = i

# k = 1 -> dp[n][1] = 1
for i in range(n+1):
    dp[i][1] = 1

# dp[n][k] = dp[n-1][k-1] + dp[n-2][k-1] + ... + dp[0][k-1]
for i in range(2, n+1):
    for j in range(2, k+1):
        for l in range(i+1):
            dp[i][j] += dp[i-l][j-1]
            dp[i][j] %= MOD

print(dp[n][k])