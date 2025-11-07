"""
* Problem   : 10872
* Title     : 팩토리얼
* Link      : https://www.acmicpc.net/problem/10872
* Category  : Math > Factorial
"""

def factorial(n:int):
    if(n == 0 or n==1):
        return 1
    return n * factorial(n-1)

num = int(input())
print(factorial(num))