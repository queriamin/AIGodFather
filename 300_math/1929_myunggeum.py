"""
* Problem   : 1929
* Title     : 소수 구하기
* Link      : https://www.acmicpc.net/problem/1929
* Category  : Math > Prime Number
"""
import math 

m,n = [int(x) for x in input().split()]

nums = [1 for _ in range(n+1)]
nums[1] = 0

root_n = int(math.sqrt(n))

# 에라토스테네스의 채를 활용하면서 range 범위를 최적화하는 게 중요하다
for i in range(2,root_n + 1):
    if nums[i] == 1:
        for j in range(i*i, n+1, i):
            nums[j] = 0

for i in range(m, n+1):
    if nums[i] == 1:
        print(i)