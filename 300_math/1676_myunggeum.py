"""
* Problem   : 10872
* Title     : 팩토리얼
* Link      : https://www.acmicpc.net/problem/1676
* Category  : Math > Factorial
"""
MAX_NUM = 500
factorial = [1 for _ in range(MAX_NUM+1)]

for i in range(1, MAX_NUM+1):
    factorial[i] = factorial[i-1] * i

def countZeros(num):
    cnt = 0
    while(num%10 == 0):
        num = num//10
        cnt += 1
    return cnt

n = int(input())
print(countZeros(factorial[n]))