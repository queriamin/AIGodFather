"""
* Problem   : 11727
* Title     : 2×n 타일링 2
* Link      : https://www.acmicpc.net/problem/11727
* Category  : Dynamic Programming
"""

class twoNTiling:
    def __init__(self) -> None:
        self.tiling_memo = [1,3]
        self.MOD = 10_007
        return
    
    def tiling(self,n):    
        if n <= len(self.tiling_memo):
            return self.tiling_memo[n-1]

        for i in range(len(self.tiling_memo), n):
            self.tiling_memo.append((self.tiling_memo[i-1] + self.tiling_memo[i-2]*2) % self.MOD)
            
        return self.tiling_memo[n-1]
    

    
tiler = twoNTiling()

N = int(input())

print(tiler.tiling(N))