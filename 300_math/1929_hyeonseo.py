from math import ceil, sqrt

M, N = map(int, input().split())

for num in range(M, N + 1):
    is_prime = True

    if num != 1:
        for j in range(2, ceil(sqrt(num))+1):
            if num % j == 0:
                is_prime = False
                break
    
    if (is_prime or num == 2) and num != 1:
        print(num)