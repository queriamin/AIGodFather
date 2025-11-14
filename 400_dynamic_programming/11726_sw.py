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
        self.tiling_memo = [1,2]
        self.MOD = 10_007
        return
    
    def tiling(self,n):    
        if n <= len(self.tiling_memo):
            return self.tiling_memo[n-1]

        for i in range(len(self.tiling_memo), n):
            self.tiling_memo.append((self.tiling_memo[i-1] + self.tiling_memo[i-2]) % self.MOD)
            
        return self.tiling_memo[n-1]
    

    
tiler = twoNTiling()

N = int(input())

print(tiler.tiling(N))