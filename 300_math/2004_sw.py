"""
* Problem   : 2004
* Title     : 조합 0의 개수
* Link      : https://www.acmicpc.net/problem/2004
* Category  : Math > Prime Factorization
"""

def combination_zeros(n: int, m: int) -> int:
    """
    르장드르 공식을 사용해 nCm의 끝자리 0의 개수를 반환합니다.
    """
    
    def count_prime_factors(k: int, p: int) -> int:
        """
        k! (k 팩토리얼) 안에 있는 소수 p의 개수를 셉니다.
        """
        count = 0
        while k >= p:
            k //= p
            count += k
        return count

    # n! / (m! * (n-m)!)
    
    # 2의 개수 계산
    two_count = count_prime_factors(n, 2) - count_prime_factors(m, 2) - count_prime_factors(n - m, 2)
    
    # 5의 개수 계산
    five_count = count_prime_factors(n, 5) - count_prime_factors(m, 5) - count_prime_factors(n - m, 5)
    
    # 10을 만들 수 있는 쌍의 개수는 2와 5의 개수 중 더 적은 값입니다.
    return min(two_count, five_count)

n,m  = [int(x) for x in input().split()]
print(combination_zeros(n,m))