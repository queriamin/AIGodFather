"""
* Problem   : 2609
* Title     : 최대공약수와 최소공배수
* Link      : https://www.acmicpc.net/problem/2609
* Category  : Math > GCD(Greatest Common Divisor), LCM (Least Common Multiple)
"""
m,n = [int(x) for x in input().split()]

gcd = 1

for i in range(1, min(m,n) + 1):
    if m%i == 0 and n%i == 0:
        gcd = i

print(gcd)
print(int(m*n/gcd))