from fractions import Fraction

a, b = map(int, input().split())

x = Fraction(a, b).numerator
y = Fraction(a, b).denominator

gcd = a // x
lcm = a * y

print(gcd)
print(lcm)