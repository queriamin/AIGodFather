# 시간초과

from math import ceil, sqrt
import sys

input = sys.stdin.readline

def is_prime_number(num):
    is_prime = True

    for j in range(2, ceil(sqrt(num))+1):
        if num % j == 0:
            is_prime = False
            break
    
    return is_prime

while True:
    num = int(input())
    if num == 0:
        break
    else:
        for i in range(3, num, 2):
            if is_prime_number(i):
                if is_prime_number(num - i):
                    print(f"{num} = {i} + {num - i}")
                    goldbach_found = True
                    break
        if not goldbach_found:
            print("Goldbach's conjecture is wrong.")