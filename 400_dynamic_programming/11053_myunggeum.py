"""
* Problem   : 11053
* Title     : 가장 긴 증가하는 부분 수열
* Link      : https://www.acmicpc.net/problem/11053
* Category  : Dynamic Programming
"""
n = int(input())
items = [int(x) for x in input().split()]

dp = [1 for i in range(n)]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if items[j] < items[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))