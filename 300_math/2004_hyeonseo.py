# 시간초과

def combination(n, r):
    small = min(r, n - r)

    realn = n
    realsmall = small

    for _ in range(small - 1):
        realn *= n - 1
        n -= 1
        realsmall *= small - 1
        small -= 1
    return realn // realsmall


n, m = map(int, input().split())
result = combination(n, m)

def zeros(F):
    count = 0

    while F >= 1:
        if F % 10 == 0:
            count += 1
            F //= 10
        else:
            break
    return count

print(zeros(result))