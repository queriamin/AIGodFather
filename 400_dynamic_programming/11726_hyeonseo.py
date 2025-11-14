tile = [1, 2] + [0 for _ in range(998)]

for i in range(2, 1000):
    tile[i] = tile[i-1] + tile[i-2]

number = int(input())
print(tile[number - 1] % 10007)