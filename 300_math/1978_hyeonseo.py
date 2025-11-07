N = int(input())

num_list = list(map(int, input().split()))
prime = 0

for i in range(N):
    num = num_list[i]
    is_prime = True

    if num != 1:
        for j in range(2, num // 2 + 1):
            if num % j == 0:
                is_prime = False
                break
    
    if is_prime and num != 1:
        prime += 1

print(prime)