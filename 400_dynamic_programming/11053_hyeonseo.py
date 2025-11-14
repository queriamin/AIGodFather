# 시간 초과
N = int(input())
A = list(map(int, input().split()))

def increasing(A):
    if len(A) == 0:
        return 0
    max_len = 1
    for i in range(len(A)):
        A_next = [x for x in A[i+1:] if x > A[i]]
        max_len = max(max_len, 1 + increasing(A_next))
    return max_len

print(increasing(A))
