N = int(input())
K = int(input())

number_list = list(range(1, N + 1))
y_list = []
idx = 0

for i in range(N):
    idx = (idx + K - 1) % len(number_list)
    y_list.append(number_list.pop(idx))

print("<", end="")
print(", ".join(map(str, y_list)), end="")
print(">", end="")