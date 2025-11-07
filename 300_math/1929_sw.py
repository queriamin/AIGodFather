"""
* Problem   : 1929
* Title     : 소수 구하기
* Link      : https://www.acmicpc.net/problem/1929
* Category  : Math > Prime Number
"""

def prime_numbers(m, n):
    primes = set([2])
    no_primes = set([1])
    for i in range(1,n+1):
        if(i in no_primes):
            continue
        else:
            if(i >= m):
                print(i)

            j = 2
            while (i * j <= n):
                no_primes.add(i*j)
                j += 1
    return

m_and_n = input()

m, n = [int(x) for x in m_and_n.split()]

prime_numbers(m,n)