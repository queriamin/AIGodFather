"""
* Problem   : 6588
* Title     : 골드바흐의 추측
* Link      : https://www.acmicpc.net/problem/6588
* Category  : Math > Prime Number
"""
from sys import stdin

primes = set()

def is_prime_number(n):
    end = int(n**(1/2))
    for i in range(2, end+1):
        if n % i == 0:
            return False
    
    return True

def check_goldbach(target_nums):    
    # primes = []
    # primes_set = set()

    for t in target_nums:
        for i, n in enumerate(range(3, t+1)):
            is_n_p = is_prime_number(n)
            is_t_m_n_p = is_prime_number(t-n)

            if(is_n_p):
                primes.add(n)

            if(is_t_m_n_p):
                primes.add(t-n)

            if(is_prime_number(n) and is_prime_number(t-n)):
                print(f"{t} = {n} + {t-n}")
                break
            
            if(i == t-3+1):
                print("Goldbach's conjecture is wrong.")
        
        # for i, p in enumerate(primes[1:]):
        #     if(t-p in primes_set):
        #         print(f"{t} = {p} + {t-p}")
        #         break

        #     if(i == len(primes)-1):
        #         print("Goldbach's conjecture is wrong.")
        
nums = []

while True:
    input_value = int(stdin.readline().rstrip())
    if input_value != 0:
        nums.append(input_value)
    else:
        break

check_goldbach(nums)
    

