"""
* Problem   : 10872
* Title     : 팩토리얼
* Link      : https://www.acmicpc.net/problem/10872
* Category  : Math > Factorial
"""
num = int(input())

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1) # 헤헤 재귀함수
    
print(factorial(num))