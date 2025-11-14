def plusway(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plusway(n - 1) + plusway(n - 2) + plusway(n - 3)

n = int(input())

for _ in range(n):
    number = int(input())
    print(plusway(number))