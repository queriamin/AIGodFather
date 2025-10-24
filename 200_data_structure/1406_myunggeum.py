"""
* Problem   : 1406
* Title     : 에디터
* Link      : https://www.acmicpc.net/problem/1406
* Category  : Data Structure > Stack
"""

import sys

# 해당 문제의 아이디어는 문제에서 얘기한 것처럼 '커서'를 움직이는 게 아니라,
# 주어지는 명령어에 따라서 문자를 '커서의 왼쪽'이나 '커서의 오른쪽'으로 옮기는 것이다

# * left_string     : 커서의 왼쪽에 위치한 문자들을 저장하는 stack
# * right_string    : 커서의 오른쪽에 위치한 문자들을 저장하는 stack
# *         -> 처음에는 커서가 문자의 가장 오른쪽에 위치해 있으므로, 모든 문자가 left_string에 저장되어 있음
left_string = list(sys.stdin.readline().rstrip()) # left stack
right_string = [] # right string

t = int(input())
for _ in range(t):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "P": # '커서의 왼쪽'에 문자 하나를 추가
      left_string.append(cmd[1])
    elif cmd[0] == "L": # 커서를 왼쪽으로 이동 == 왼쪽 문자 하나를 커서의 오른쪽으로 이동
      if len(left_string) > 0:
        right_string.append(left_string.pop())
    elif cmd[0] == "D": # 커서를 오른쪽으로 이동 == 오른쪽 문자 하나를 커서의 왼쪽으로 이동
      if len(right_string) > 0:
        left_string.append(right_string.pop())
    elif cmd[0] == "B": # '커서의 왼쪽'에 문자 하나를 삭제
      if len(left_string) > 0:
        left_string.pop()
  
# 마지막에 출력할 때 right_string은 stack 구조이므로, reverse해줘야 순서가 맞는다
print("".join(left_string + right_string[::-1]))