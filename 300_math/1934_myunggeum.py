"""
* Problem   : 1934
* Title     : 최소공배수
* Link      : https://www.acmicpc.net/problem/1934
* Category  : Math > LCM (Least Common Multiple)
"""

# LCM = (a * b) / GCD의 관계를 가진다
def find_gcd(a,b):
    gcd = 1
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd

out = []
t = int(input())

for _ in range(t):
    m,n = [int(x)  for x in input().split()]
    gcd = find_gcd(m,n)
    out.append(int(m*n/gcd))

for res in out:
    print(res)