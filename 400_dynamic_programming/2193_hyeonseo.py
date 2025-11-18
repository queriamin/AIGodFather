pinary = [1, 1] + [0 for _ in range(90)]

for i in range(2, 90):
    pinary[i] = pinary[i-1] + pinary[i-2]

number = int(input())
print(pinary[number - 1])