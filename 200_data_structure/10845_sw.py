"""
* Problem   : 10845
* Title     : 큐
* Link      : https://www.acmicpc.net/problem/10845
* Category  : Data Structure > Queue
"""

from sys import stdin
from collections import deque

class MyQueue():
    def __init__(self):
        self.queue = deque([])
        return
    
    def parse_cmd(self, command:str):
        cmd_split = command.split()
        if(cmd_split[0] == "push"):
            return self.push(int(cmd_split[1]))
        if(cmd_split[0] == "pop"):
            return self.pop()
        if(cmd_split[0] == "size"):
            return self.size()
        if(cmd_split[0] == "empty"):
            return self.empty()
        if(cmd_split[0] == "front"):
            return self.front()
        if(cmd_split[0] == "back"):
            return self.back()
        
        
    def push(self, x:int):
        self.queue.append(x)

    def pop(self):
        if(self.queue):
            print(self.queue.popleft())
            return 
        
        print(-1)
        return 

    def size(self):
        print(len(self.queue))
        return 
    
    def empty(self):
        if len(self.queue):
            print(0)
        else:
            print(1)
    
    def front(self):
        if (self.queue):
            print(self.queue[0])
        else:
            print(-1)
    
    def back(self):
        if (self.queue):
            print(self.queue[-1])
        else:
            print(-1)

num_cmds = int(input())

queue = MyQueue()

for _ in range(num_cmds):
    queue.parse_cmd(stdin.readline().rstrip())

