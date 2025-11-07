from fractions import Fraction

def lcm(a, b):
    y = Fraction(a, b).denominator
    lcm = a * y
    return lcm

N = int(input())
for n in range(N):
    a, b = map(int, input().split())
    print(lcm(a, b))