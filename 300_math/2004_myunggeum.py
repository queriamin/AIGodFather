"""
* Problem   : 2004
* Title     : 조합 0의 개수
* Link      : https://www.acmicpc.net/problem/2004
* Category  : Math > Prime Factorization
"""
def prime_factorize(num, k):
    cnt = 0
    while(num):
        num //= k
        cnt += num
    return cnt

n, m = [int(x) for x in input().split()]

factorize_two = prime_factorize(n, 2) - prime_factorize(m, 2) - prime_factorize(n-m, 2)
factorize_five = prime_factorize(n, 5) - prime_factorize(m, 5) - prime_factorize(n-m, 5)

print(min(factorize_two, factorize_five))