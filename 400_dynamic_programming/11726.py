"""
* Problem   : 11726
* Title     : 2×n 타일링
* Link      : https://www.acmicpc.net/problem/11726
* Category  : Dynamic Programming
"""

class twoNTiling:
    def __init__(self) -> None:
        self.plan_count = 0
        pass

    def tiling_plan(self, target_n):
        self.tiling_plan_helper(1, target_n)
        self.tiling_plan_helper(2, target_n)
        return self.plan_count
    
    def tiling_plan_helper(self, column_count, target_n):
        if(column_count == target_n):
            self.plan_count += 1 
        elif(column_count < target_n):
            self.tiling_plan_helper(column_count+1, target_n)
            self.tiling_plan_helper(column_count+2, target_n)
        else:
            return

    
tiler = twoNTiling()

N = int(input())

