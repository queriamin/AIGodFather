"""
* Problem   : 10866
* Title     : 덱
* Link      : https://www.acmicpc.net/problem/10866
* Category  : Data Structure > Dequeue
"""
import sys

class Dequeue:
    def __init__(self):
        self.mem = []
        
    def push_front(self, item):
        self.mem.insert(0, item)

    def push_back(self, item):
        self.mem.append(item)
    
    def pop_front(self):
        if not self.mem:
            return -1
        else:
            front = self.mem[0]
            del self.mem[0]
            return front
    
    def pop_back(self):
        return -1 if not self.mem else self.mem.pop()

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

deq = Dequeue()
for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    
    if cmd == "push_back":
        deq.push_back(parts[1])
    elif cmd == "push_front":
        deq.push_front(parts[1])
    elif cmd == "pop_front":
        out.append(deq.pop_front())
    elif cmd == "pop_back":
        out.append(deq.pop_back())
    elif cmd == "size":
        out.append(deq.size())
    elif cmd == "empty":
        out.append(deq.empty())
    elif cmd == "front":
        out.append(deq.front())
    else:
        out.append(deq.back())

sys.stdout.write("\n".join([str(x) for x in out]))