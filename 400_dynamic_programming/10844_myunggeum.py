"""
* Problem   : 10844
* Title     : 쉬운 계단 수
* Link      : https://www.acmicpc.net/problem/10844
* Category  : Dynamic Programming
"""
n = int(input())

# n 자리 수가 있고, 각 자리에는 0~9까지의 수가 들어갈 수 있다
# cnts[i][j] : i자리수 중에서 i번째 자리가 j인 수의 개수
cnts = [[0] * 10 for _ in range(n)]

for i in range(10):
    cnts[0][i] = 1

for i in range(1,n):
    for k in range(1,9): # 계단수이려면 본인 왼쪽의 수보다 1 크거나 1 작아야 함
        cnts[i][k] = (cnts[i-1][k-1] + cnts[i-1][k+1])%1e+9
    cnts[i][0] = cnts[i-1][1]%1e+9 # 0의 왼쪽에는 1밖에 올 수 없고
    cnts[i][9] = cnts[i-1][8]%1e+9 # 9의 왼쪽에는 8밖에 올 수 없음

result = 0
for i in range(1,10):
    result += (cnts[n-1][i])%1e+9
print(int(result%1e+9))