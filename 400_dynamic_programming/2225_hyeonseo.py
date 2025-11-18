# 시간 초과
def decompose_sum(n, k):
    if k == 1:
        return 1
    else:
        return sum(decompose_sum(n - i, k - 1) for i in range(n + 1))

N, K = map(int, input().split())
print(decompose_sum(N, K))