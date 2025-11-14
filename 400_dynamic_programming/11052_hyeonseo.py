# 틀렸습니다
N = int(input())
P = list(map(float, input().split()))

for i in range(len(P)):
    P[i] = P[i]/(i + 1)

result = 0

while True:
    if N > 0:
        max_P = max(P[:(N+1)])
        max_i = P.index(max_P) + 1
        result += max_P * max_i
        N -= max_i
    else:
        break

print(int(result))