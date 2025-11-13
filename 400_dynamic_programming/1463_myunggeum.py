"""
* Problem   : 1463
* Title     : 1로 만들기
* Link      : https://www.acmicpc.net/problem/1463
* Category  : Dynamic Programming
"""
n = int(input())

dp = [0] * (n+1)

dp[1] = 0
if n >= 2:
    dp[2] = 1
if n >= 3:
    dp[3] = 1

    for i in range(4,n+1):
        if i%6==0 : # 3으로도 나누어 떨어지고, 2로도 나누어 떨어질 때
            dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)
        elif i%3==0 : # 3으로만 나누어 떨어질 때
            dp[i] = min(dp[i//3]+1, dp[i-1]+1)
        elif i%2==0 : # 2로만 나누어 떨어질 때
            dp[i] = min(dp[i//2]+1, dp[i-1]+1)
        else: # 3과 2 모두 나누어 떨어지지 않을 때
            dp[i] = dp[i-1] + 1