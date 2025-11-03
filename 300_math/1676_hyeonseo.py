# VS Code에서는 틀림

N = int(input())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

F = factorial(N)
count = 0

while F >= 1:
    if F % 10 == 0:
        count += 1
        F //= 10
    else:
        break

print(count)