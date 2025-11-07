"""
* Problem   : 1929
* Title     : 소수 구하기
* Link      : https://www.acmicpc.net/problem/1929
* Category  : Math > Prime Number
"""

m, n = map(int, input().split())
# print(m, n)
res = []                        # 맨 마지막에 res.append(num)을 하려고 했더니
                                # 문제에서 요구하는 출력 형태랑 안 맞음

def is_prime(num):                      
    if num == 1:                        
        return False
    elif num == 2:                      
        return True
    for i in range(2, int(num**0.5) + 1):       # 분명 timeouterror가 뜰 거 같은데 (응...)         
        if num % i == 0:                        # 그래서 제곱근까지로 해봤더니 통과함!!
            return False                
    return True

for num in range(m, n+1):
    if is_prime(num):           # 이게 true면 실행되는 코드라는 거지
        print(num)
