import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    sentence = list(input().split(" "))
    for s in sentence:
        print(s[::-1], end=" ")
    print()