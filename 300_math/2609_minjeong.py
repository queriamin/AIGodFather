"""
* Problem   : 2609
* Title     : 최대공약수와 최소공배수
* Link      : https://www.acmicpc.net/problem/2609
* Category  : Math > GCD(Greatest Common Divisor), LCM (Least Common Multiple)
"""

a, b = map(int, input().split())
# print(a,b) # 헤헤 혹시 모르니까 확인
# print(max(a,b)) # 혹시 몰라서 또 확인

# 최대공약수 구하기
GCD = []
div = 1

for _ in range(min(a, b)):
    if a%div == 0 and b%div == 0:   # 둘 다 나머지가 0이라면(나누어 떨어진다면)
        GCD.append(div)             # GCD 리스트에 해당 공약수를 추가하고
        div += 1                    # 다음 수로 넘어가기
    else:
        div += 1                    # 안되면 바로 넘어가기

print(GCD[-1])                      # 가장 큰 값 출력하기


# 최소공배수 구하기
print(a*b//GCD[-1])                 # 최소공배수는 공식이 있다고 하네...?
                                    # A*B//최대공약수 하면 최소공배수래
