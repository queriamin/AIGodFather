"""
* Problem   : 6588
* Title     : 골드바흐의 추측
* Link      : https://www.acmicpc.net/problem/6588
* Category  : Math > Prime Number
"""
from sys import stdin

primes = set()

def prime_numbers(n):
    prime_numbers = list(range(1,n+1))
    prime_numbers[0] = 0
    
    pointer = 0
    while pointer < n:
        if(prime_numbers[pointer] == 0):
            pointer += 1
            continue
        else:
            p_n = prime_numbers[pointer]
            tmp_pointer = p_n + pointer
            while(tmp_pointer < n):
                prime_numbers[tmp_pointer] = 0
                tmp_pointer += p_n
            
            pointer += 1
            
    
    prime_numbers = [p for p in prime_numbers if p != 0]

    return prime_numbers


def check_goldbach(nums):
    for n in nums:
        for i in range(1, n+1):
            if(i in primes and (n-i) in primes):
                print(f"{n} = {i} + {n-i}")
                break
            if(i == n):
                print("fuck")




nums = []

while True:
    input_value = int(stdin.readline().rstrip())
    if input_value != 0:
        nums.append(input_value)
    else:
        break

primes = set(prime_numbers(max(nums)))

check_goldbach(nums)
    

