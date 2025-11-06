"""
* Problem   : 1978
* Title     : 소수 찾기
* Link      : https://www.acmicpc.net/problem/1978
* Category  : Math > Prime Number
"""

num_case = int(input())                 # 이건 안필요하지 않아?
nums = list(map(int, input().split()))  # 리스트에 정수 넣기
# print(num_case, nums)                 # 잘 들어갔는지 확인
answer = 0                              # 마지막에 프린트 할 값

def is_prime(num):                      # 함수로 써봄
    if num == 1:                        # 1은 소수가 아님
        return False
    elif num == 2:                      # 2는 따로 체크하는 게 나은 듯
        return True
    for i in range(2, num):             # 2에서부터 num-1까지의 숫자 중
        if num % i == 0:                # 나누어 떨어지는 값이 있으면
            return False                # 소수가 아님
    return True                         # 모두 통과하면 소수임(1, 2가 아니고 2~num-1의 값으로 나누어지지 않음)


for num in nums:                        # 주어진 리스트 순회하면서
    return_value = is_prime(num)        # true이면 answer에 1 추가
    if return_value == True:        
        answer += 1                     # **요길 더 깔끔하게 쓰는 법 궁금함**

print(answer)