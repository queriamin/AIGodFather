"""
* Problem   : 1978
* Title     : 소수 찾기
* Link      : https://www.acmicpc.net/problem/1978
* Category  : Math > Prime Number
"""

def is_prime(k):
    if k == 1:
        return 0

    for i in range(2,k):
        if k%i == 0:
            return 0
    return 1

n = int(input())
nums = [int(x) for x in input().split()]
res = [is_prime(x) for x in nums]

print(sum(res))