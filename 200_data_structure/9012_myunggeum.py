"""
* Problem   : 9012
* Title     : 괄호
* Link      : https://www.acmicpc.net/problem/9012
* Category  : Data Structure > Stack
"""
import sys

class Stack:
    def __init__(self):
        self.mem = []
    
    def push(self, item):
        self.mem.append(item)
    
    def pop(self):
        return -1 if not self.mem else self.mem.pop()
    
    def size(self):
        return len(self.mem)

    def empty(self):
        return 0 if self.mem else 1
    
    def top(self):
        return self.mem[-1] if self.mem else -1
    
n = int(sys.stdin.readline())
out = []

for _ in range(n):
    cmds = input()

    stack = Stack()
    for item in cmds:
        if item == "(": # 열린 괄호 "(" 일때는 스택에 넣고
            stack.push(item)
        elif item == ")" and stack.top() == "(": # 괄호 쌍이 매칭되면 pop
            stack.pop()
        else: # 이외 : 열린 괄호가 없는 데 닫힌 괄호가 들어온 경우
            stack.push(item)
        
    # 스택 안에서 괄호 쌍이 성공적으로 매칭이 되었다면, 아무것도 남아있어서는 안된다
    if stack.empty():
        out.append("YES")
    else: # 뭐라도 남아있다면 실패했다는 의미
        out.append("NO")

sys.stdout.write("\n".join(out))