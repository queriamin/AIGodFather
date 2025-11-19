"""
* Problem   : 10844
* Title     : 쉬운 계단 수
* Link      : https://www.acmicpc.net/problem/10844
* Category  : Dynamic Programming
"""
n = int(input())

cnts = [[0] * 10 for _ in range(n)]

for i in range(10):
    cnts[0][i] = 1

for i in range(1,n):
    for k in range(1,9):
        cnts[i][k] = (cnts[i-1][k-1] + cnts[i-1][k+1])%1e+9
    cnts[i][0] = cnts[i-1][1]%1e+9
    cnts[i][9] = cnts[i-1][8]%1e+9

result = 0
for i in range(1,10):
    result += (cnts[n-1][i])%1e+9
print(int(result%1e+9))