"""
* Problem   : 1912
* Title     : 연속합
* Link      : https://www.acmicpc.net/problem/1912
* Category  : Dynamic Programming
"""
n = int(input())
nums = [int(x) for x in input().split()]

dp = [0] * n
result = nums[0]
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])
    result = max(dp[i], result)
        
print(result)