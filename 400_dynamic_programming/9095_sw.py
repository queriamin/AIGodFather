"""
* Problem   : 9095
* Title     : 1, 2, 3 더하기
* Link      : https://www.acmicpc.net/problem/9095
* Category  : Dynamic Programming
"""

from sys import stdin

class Adder:
    def __init__(self) -> None:
        self.ways_count = 0        
        return 

    def num_maker(self, target:int):
        self.num_maker_helper(target, 0)
        return self.ways_count
    
    def reset_count(self):
        self.ways_count = 0
        return

    def num_maker_helper(self, target, wip:int):
        if(wip == target):
            self.ways_count += 1
        elif(wip > target):
            return
        else:
            self.num_maker_helper(target, wip+1)
            self.num_maker_helper(target, wip+2)
            self.num_maker_helper(target, wip+3)

        return
    


N = int(input())
adder = Adder()

for _ in range(N):
    adder.reset_count()
    print(adder.num_maker(int(stdin.readline().rstrip())))
    