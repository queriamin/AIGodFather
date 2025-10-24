"""
* Problem   : 10845
* Title     : 큐
* Link      : https://www.acmicpc.net/problem/10845
* Category  : Data Structure > Queue
"""

import sys

class Queue:
    def __init__(self):
        self.mem = []
    
    def push(self, item):
        self.mem.append(item)
    
    def pop(self):
        if not self.mem:
            return -1
        else:
            front = self.front()
            del self.mem[0]
            return front
        
    def size(self):
        return len(self.mem)
    
    def empty(self):
        return 0 if self.mem else 1
    
    def front(self):
        return self.mem[0] if self.mem else -1
    
    def back(self):
        return self.mem[-1] if self.mem else -1
    
n = int(sys.stdin.readline())
out = []

queue = Queue()
for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    
    if cmd == "push":
        queue.push(parts[1])
    elif cmd == "front":
        out.append(queue.front())
    elif cmd == "back":
        out.append(queue.back())
    elif cmd == "size":
        out.append(queue.size())
    elif cmd == "empty":
        out.append(queue.empty())
    else:
        out.append(queue.pop())

sys.stdout.write("\n".join([str(x) for x in out]))

