"""
* Problem   : 1978
* Title     : 소수 찾기
* Link      : https://www.acmicpc.net/problem/1978
* Category  : Math > Prime Number
"""

def prime_numbers(n):
    # print(n)
    primes = set()
    no_primes = set([1])
    for i in range(1,n+1):
        if(i in no_primes):
            continue
        else:
            primes.add(i)
            # print(primes)
            j = 2
            while (i * j <= n):
                no_primes.add(i*j)
                j += 1
    return primes

def count_primes(nums):
    primes = prime_numbers(max(nums))
    count = 0
    for n in nums:
        if n in primes:
            count += 1
    
    print(count)
    return


N = int(input())
count_primes([int(x) for x in input().split()])
    


