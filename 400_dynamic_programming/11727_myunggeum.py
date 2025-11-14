"""
* Problem   : 11727
* Title     : 2×n 타일링 2
* Link      : https://www.acmicpc.net/problem/11727
* Category  : Dynamic Programming
"""
n = int(input())

dp = [0] * (n+10)
dp[1] = 1
dp[2] = 3

# +--+
# |  | (i-1)
# +--+

# +----+
# +----+ (i-2)
# +----+

# +----+
# |    | (i-2)
# +----+

for i in range(3, n+1):
    dp[i] = (dp[i-2]*2 + dp[i-1])%10007

print(dp[n]%10007)