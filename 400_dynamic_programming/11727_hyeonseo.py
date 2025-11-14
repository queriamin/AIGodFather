tile = [1] + [0 for _ in range(999)]

for i in range(1, 1000):
    if i % 2 == 0:
        tile[i] = 2 * tile[i-1] - 1
    else:
        tile[i] = 2 * tile[i-1] + 1

number = int(input())
print(tile[number - 1] % 10007)