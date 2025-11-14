"""
* Problem   : 11052
* Title     : 카드 구매하기
* Link      : https://www.acmicpc.net/problem/11052
* Category  : Dynamic Programming
"""
n = int(input())
deck = [int(x) for x in input().split()]

dp = [0] * (n+1)
dp[1] = deck[0]

# 아이디어 : dp[i] : i개의 카드를 사는데 최댓값을 저장
# dp[i+1] = max(dp[i] + 1개카드팩, dp[i-1], 2개카드팩, ...)

for i in range(2,n+1):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[i-j] + deck[j-1])
    dp[i] = max(dp[i], deck[i-1])

print(dp[n])