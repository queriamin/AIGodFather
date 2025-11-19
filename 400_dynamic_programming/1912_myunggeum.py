"""
* Problem   : 1912
* Title     : 연속합
* Link      : https://www.acmicpc.net/problem/1912
* Category  : Dynamic Programming
"""
n = int(input())
nums = [int(x) for x in input().split()]

dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    # dp[i-1] : 나 이전까지의 연속된 수의 합에다가 나를 포함할지
    # nums[i] : 나부터 새로운 연속된 수 합을 만들기 시작할지
    dp[i] = max(dp[i-1] + nums[i], nums[i])
        
print(max(dp))