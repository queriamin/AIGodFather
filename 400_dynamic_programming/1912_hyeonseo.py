# 시간 초과
n = int(input())
li = list(map(int, input().split()))
max_li = []

for i in range(1, n):
    sum_li = []
    for j in range(n - i + 1):
        sum_li.append(sum(li[j:j+i]))
    max_li.append(max(sum_li))

print(max(max_li))