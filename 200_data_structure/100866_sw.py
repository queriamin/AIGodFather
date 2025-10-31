"""
* Problem   : 10866
* Title     : 덱
* Link      : https://www.acmicpc.net/problem/10866
* Category  : Data Structure > Dequeue
"""


from sys import stdin
from collections import deque

class MyDeque():
    def __init__(self):
        self.dq = deque([])
        return
    
    def parse_cmd(self, command:str):
        cmd_split = command.split()
        if(cmd_split[0] == "push_front"):
            return self.push_front(int(cmd_split[1]))
        if(cmd_split[0] == "push_back"):
            return self.push_back(int(cmd_split[1]))
        if(cmd_split[0] == "pop_front"):
            return self.pop_front()
        if(cmd_split[0] == "pop_back"):
            return self.pop_back()
        if(cmd_split[0] == "size"):
            return self.size()
        if(cmd_split[0] == "empty"):
            return self.empty()
        if(cmd_split[0] == "front"):
            return self.front()
        if(cmd_split[0] == "back"):
            return self.back()
        
        
    def push_front(self, x:int):
        self.dq.appendleft(x)
    
    def push_back(self, x:int):
        self.dq.append(x)

    def pop_front(self):
        if(self.dq):
            print(self.dq.popleft())
            return 
        print(-1)
        return 

    def pop_back(self):
        if(self.dq):
            print(self.dq.pop())
            return 
        print(-1)
        return 
    

    
    def size(self):
        print(len(self.dq))
        return 
    
    def empty(self):
        if len(self.dq):
            print(0)
        else:
            print(1)
    
    def front(self):
        if (self.dq):
            print(self.dq[0])
        else:
            print(-1)
    
    def back(self):
        if (self.dq):
            print(self.dq[-1])
        else:
            print(-1)

num_cmds = int(input())

queue = MyDeque()

for _ in range(num_cmds):
    queue.parse_cmd(stdin.readline().rstrip())

