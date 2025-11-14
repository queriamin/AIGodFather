"""
* Problem   : 9095
* Title     : 1, 2, 3 더하기
* Link      : https://www.acmicpc.net/problem/9095
* Category  : Dynamic Programming
"""
n = int(input())
test = []
for i in range(n):
    test.append(int(input()))

def f(i):
    if i==1:
        return 1
    elif i==2:
        return 2
    elif i==3:
        return 4 # 1+1+1 1+2 2+1 3
    else:
        return f(i-1) + f(i-2) + f(i-3)
   
for i in range(n):
    print(f(test[i]))