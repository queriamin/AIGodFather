# 틀렸습니다
N = int(input()) - 1

if N == 0:
    print(9)
else:
    result = 19 * N - 4 * N * N
    x = 0

    for _ in range(N):
        x += N
        N += 1

    result += 2 * x
    print(result)