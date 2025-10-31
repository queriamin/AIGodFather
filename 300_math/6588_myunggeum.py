"""
* Problem   : 6588
* Title     : 골드바흐의 추측
* Link      : https://www.acmicpc.net/problem/6588
* Category  : Math > Prime Number
"""
# sys.stdin 으로 처리하지 않으면 시간초과 발생함
import sys

MAX_NUM = 10**6
ROOT_MAX_NUM = int(MAX_NUM**0.5)

isPrime = [1 for _ in range(MAX_NUM+1)]
isPrime[0] = isPrime[1] = 0

for i in range(2, ROOT_MAX_NUM+ 1):
    if isPrime[i] == 1:
        for j in range(i*i, MAX_NUM+1, i):
            isPrime[j] = 0

def goldbachConjecture(num):
    for i in range(3, int(num/2)+1, 2):
        if isPrime[i] and isPrime[num-i]:
            return i, num-i
    return 0,num

out = []
test_case = 1
while(test_case != 0):
    test_case = int(sys.stdin.readline())
    if test_case == 0:
        break

    a,b = goldbachConjecture(test_case)
    if a == 0:
        out.append("Goldbach's conjecture is wrong.\n")
    else:
        out.append(f"{test_case} = {a} + {b}\n")


sys.stdout.write(''.join(out))