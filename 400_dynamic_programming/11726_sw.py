"""
* Problem   : 11726
* Title     : 2×n 타일링
* Link      : https://www.acmicpc.net/problem/11726
* Category  : Dynamic Programming
"""

# class twoNTiling:
#     def __init__(self) -> None:
#         self.plan_count_dict = {0:0, 1:1, 2:2}
#         return

#     def tiling_plan(self, target_n):
#         for i in range(1, target_n+1):
#             self.tiling_plan_helper(i)
#         # self.tiling_plan_helper(1, target_n)
#         # self.tiling_plan_helper(2, target_n)
#         return self.plan_count_dict[target_n]
    
#     def tiling_plan_helper(self, n_columns):
#         if(n_columns)


class twoNTiling:
    def __init__(self) -> None:
        self.plan_count = 0
        return

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

print(tiler.tiling_plan(N))