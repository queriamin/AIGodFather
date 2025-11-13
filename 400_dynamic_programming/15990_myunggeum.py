"""
* Problem   : 15990
* Title     : 1, 2, 3 더하기 5
* Link      : https://www.acmicpc.net/problem/15990
* Category  : Dynamic Programming
"""
t = int(input())

MAX_NUM = 10**5
MOD = 1000000009
dp = [[0,0,0]] * (MAX_NUM+1)

dp[1] = [1,0,0] # 1
dp[2] = [0,1,0] # 2
dp[3] = [1,1,1] # 1+2 2+1 3

dp[4] = [2,0,1] # 1+2+1 1+3 3+1
dp[5] = [1,2,1] # 1+3+1 2+3 2+1+2 3+2

for i in range(6, MAX_NUM+1):
    dp[i] = [(dp[i-1][1] + dp[i-1][2]) % MOD, (dp[i-2][0] + dp[i-2][2]) % MOD, (dp[i-3][0] + dp[i-3][1]) % MOD]
    
out = []
for _ in range(t):
    n = int(input())
    out.append(sum(dp[n])%MOD)

for o in out:
    print(o)
