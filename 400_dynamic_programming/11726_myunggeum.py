"""
* Problem   : 11726
* Title     : 2×n 타일링
* Link      : https://www.acmicpc.net/problem/11726
* Category  : Dynamic Programming
"""
n = int(input())

dp = [[0] for i in range(n+10)]
dp[1] = 1
dp[2] = 2

# +--+
# |  | (i-1)
# +--+

# +----+
# +----+ (i-2)
# +----+

for i in range(3,n+1):
    dp[i] = (dp[i-2] + dp[i-1])%10007

print(dp[n]%10007)