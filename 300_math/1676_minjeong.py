"""
* Problem   : 10872
* Title     : 팩토리얼
* Link      : https://www.acmicpc.net/problem/10872
* Category  : Math > Factorial
"""
num = int(input())

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1) # 헤헤 재귀함수
    
res = str(factorial(num))

ans = 0                                 # 결과로 보고 싶은 게 두 개면 변수명을...?

for r in reversed(res):                 # 뒤에서부터 0의 갯수 세기
    # print(r)
    if r == "0":                        # str로 바꿔놔서 "0"으로 세야 함
        ans += 1
    else:
        break                           # 다른 숫자를 만나면 break
        
print(ans)

