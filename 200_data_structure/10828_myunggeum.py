"""
* Problem   : 10828
* Title     : 스택
* Link      : https://www.acmicpc.net/problem/10828
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
    
stack = Stack()

# python에서 입력을 처리할 때 (1) input()으로 받거나
# (2) sys library에서 sys.stdin.readline()으로 받을 수 있는데
# (1)의 경우 라이브러리 없이 사용하기에 많이들 이용하지만, 입력이 길거나 문제에 제한시간이 빡빡한 경우
# (2)을 이용해서 풀면 해결되는 경우가 있다

n = int(sys.stdin.readline()) 
out = []

for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    if cmd == 'push':
        stack.push(int(parts[1]))
    elif cmd == 'pop':
        out.append(str(stack.pop()))
    elif cmd == 'size':
        out.append(str(stack.size()))
    elif cmd == 'empty':
        out.append(str(stack.empty()))
    elif cmd == 'top':
        out.append(str(stack.top()))

sys.stdout.write("\n".join(out))