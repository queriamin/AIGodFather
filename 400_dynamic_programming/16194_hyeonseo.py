# 틀렸습니다
N = int(input())
P = list(map(float, input().split()))

for i in range(len(P)):
    P[i] = P[i]/(i + 1)

result = 0

while True:
    if N > 0:
        min_P = min(P[:(N+1)])
        min_i = P.index(min_P) + 1
        result += min_P * min_i
        N -= min_i
    else:
        break

print(int(result))