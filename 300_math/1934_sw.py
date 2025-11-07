"""
* Problem   : 1934
* Title     : 최소공배수
* Link      : https://www.acmicpc.net/problem/1934
* Category  : Math > LCM (Least Common Multiple)
"""

from sys import stdin

def gcm(a:int, b:int):
    mod = max(a,b) % min(a,b)
    if(mod == 0):
        return min(a,b)
    else:
        return gcm(min(a,b), mod)

def lcm(a:int, b:int):    
    return int(a * b / gcm(a,b))


N = int(input())


for _ in range(N):
    a, b = [int(x) for x in (stdin.readline().rstrip()).split()]
    
    print(lcm(a,b))