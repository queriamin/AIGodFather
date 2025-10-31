"""
* Problem   : 10872
* Title     : 팩토리얼
* Link      : https://www.acmicpc.net/problem/10872
* Category  : Math > Factorial
"""
MAX_NUM = 12
factorial = [1 for _ in range(MAX_NUM+1)]

for i in range(1, MAX_NUM+1):
    factorial[i] = factorial[i-1] * i

n = int(input())
print(factorial[n])