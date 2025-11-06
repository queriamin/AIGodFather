"""
* Problem   : 1934
* Title     : 최소공배수
* Link      : https://www.acmicpc.net/problem/1934
* Category  : Math > LCM (Least Common Multiple)
"""

# 앞 문제랑 거의 똑같은데 최소공배수만 다루고 test case가 여러 개라는 점이 다름
# 근데 중첩 for문이라 이렇게 하지 말라고 배움 -> 실제로 시간 초과됨

num_case = int(input())

for _ in range(num_case):
    a, b = map(int, input().split())
    GCD = []
    div = 1

    for _ in range(min(a, b)):
        if a%div == 0 and b%div == 0: 
            GCD.append(div)             
            div += 1                   
        else:
            div += 1   

    print(a*b//GCD[-1])


