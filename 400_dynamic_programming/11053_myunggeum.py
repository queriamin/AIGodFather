"""
* Problem   : 11053
* Title     : 가장 긴 증가하는 부분 수열
* Link      : https://www.acmicpc.net/problem/11053
* Category  : Dynamic Programming
"""
n = int(input())
items = [int(x) for x in input().split()]

# i번째 요소까지 봤을 때 가장 긴 증가하는 부분 수열의 길이
dp = [1 for _ in range(n)]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if items[j] < items[i]: # 나보다 앞에 있는 요소의 크기가 작은 것들 중
            dp[i] = max(dp[i], dp[j] + 1) # 내가 추가되었을 때 가장 큰 경우를 채택

print(max(dp))