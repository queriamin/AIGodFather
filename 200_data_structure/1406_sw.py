
"""
* Problem   : 1406
* Title     : 에디터
* Link      : https://www.acmicpc.net/problem/1406
* Category  : Data Structure > Stack
"""

from collections import deque
from sys import stdin

class Editor():
    def __init__(self, init_string:str) -> None:
        self.left_deque = deque([x for x in init_string])
        self.right_deque = deque([])
    
    def parse_cmd(self, command:str):
        cmd_split = command.split()
        if(cmd_split[0] == "L"):
            return self.left_shift()
        if(cmd_split[0] == "D"):
            return self.right_shift()
        if(cmd_split[0] == "P"):
            return self.put(cmd_split[1])
        if(cmd_split[0] == "B"):
            return self.delete_chr()
        
    def left_shift(self):
        if(len(self.left_deque)):
            tmp = self.left_deque.pop()
            self.right_deque.appendleft(tmp)
        return
    
    def right_shift(self):
        if(len(self.right_deque)):
            self.left_deque.append(self.right_deque.popleft())
        return

    def delete_chr(self):
        if(len(self.left_deque)):
            self.left_deque.pop()
        return 

    def put(self, c):
        self.left_deque.append(c)
        # print(self.left_deque)
        return

    def print_str(self):
        string = "".join(self.left_deque) + "".join(self.right_deque)
        print(string)
        return string
    

init_string = input()
num_cmds = int(input())

editor = Editor(init_string)

for _ in range(num_cmds):
    editor.parse_cmd(stdin.readline().rstrip())

editor.print_str()