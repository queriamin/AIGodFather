"""
* Problem   : 16194
* Title     : 카드 구매하기 2
* Link      : https://www.acmicpc.net/problem/16194
* Category  : Dynamic Programming
"""
n = int(input())
deck = [int(x) for x in input().split()]

dp = [10001] * (n+1)
dp[1] = deck[0]

# 11052 문제랑 동일한 풀이인데
# (1) dp에 initialize할 때 maximum으로 저장
# (2) dp를 update할 때 minimum 이용

for i in range(2,n+1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j] + deck[j-1])
    dp[i] = min(dp[i], deck[i-1])

print(dp[n])