"""
* Problem   : 2193
* Title     : 이친수
* Link      : https://www.acmicpc.net/problem/2193
* Category  : Dynamic Programming
"""
n = int(input())

# n자리 이친수의 개수를 저장하고 있는 배열 dp
dp = [1 for _ in range(100)]

dp[1] = 1 # 1 
dp[2] = 1 # 10
dp[3] = 2 # 101 100

# n자리의 이친수 = (n-2)자리 이친수 끝에   01
#             + (n-3)자리 이친수 끝에  010
#             + (n-4)자리 이친수 끝에 0100
#             + ...
#             +  1   자리 이친수 끝에 010...0

if n > 3:
    for i in range(4,n+1):
        for j in range(2,i):
            dp[i] += dp[i-j]

print(dp[n])
