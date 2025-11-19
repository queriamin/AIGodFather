"""
* Problem   : 14002
* Title     : 가장 긴 증가하는 부분 수열 4
* Link      : https://www.acmicpc.net/problem/14002
* Category  : Dynamic Programming
"""
n = int(input())
arr = [int(x) for x in input().split()]

dp = [1] * n
save = [[]] * n

for i in range(n):
    save[i] = [arr[i]]
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[j] + 1 > dp[i]:
                new_arr = save[j].copy()
                new_arr.append(arr[i])
                save[i] = new_arr
                dp[i] = dp[j] + 1

max_idx = dp.index(max(dp))

print(max(dp))
print(" ".join([str(x) for x in save[max_idx]]))