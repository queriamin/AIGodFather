"""
* Problem   : 1463
* Title     : 1로 만들기
* Link      : https://www.acmicpc.net/problem/1463
* Category  : Dynamic Programming
"""

class OneMaker:
    def __init__(self) -> None:
        self.min_op_count = 10e+7
        return 

    def one_maker(self, x:int):
        self.one_maker_helper(x, 0)
        return self.min_op_count

    def one_maker_helper(self, x:int, op_count):
        #base case
        if(x == 1):
            self.min_op_count = min(self.min_op_count, op_count)
            return

        if(op_count >= self.min_op_count):
            return

        #recursive
        if(x % 3 == 0):
            self.one_maker_helper(x//3, (op_count+1))
        if(x % 2 == 0):
            self.one_maker_helper(x//2, (op_count+1))
        
        self.one_maker_helper(x-1, (op_count+1))

        return


one_maker = OneMaker()

num = int(input())
print(one_maker.one_maker(num))