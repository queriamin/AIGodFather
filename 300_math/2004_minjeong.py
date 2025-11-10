def is_factor(num, factor):
    count = 0
    while num:
        num  //= factor
        count += num
    return count

n, m = map(int, input().split())
# print(n,m)

two = is_factor(n,2) - is_factor(m,2) - is_factor(n-m, 2)
five = is_factor(n,5) - is_factor(m,5) - is_factor(n-m, 5)

print(min(two, five))