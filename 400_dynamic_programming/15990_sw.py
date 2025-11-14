"""
* Problem   : 15990
* Title     : 1, 2, 3 더하기 5
* Link      : https://www.acmicpc.net/problem/15990
* Category  : Dynamic Programming
"""
from sys import stdin

class OTT:
    def __init__(self) -> None:
        # 1. Define the modulo constant
        self.MOD = 1_000_000_009 
        
        self.sum_ways = [
            (1, 0, 0), # n=1
            (0, 1, 0), # n=2
            (1, 1, 1)  # n=3
        ] 
        #(1로 끝나는 경우, 2로 끝나는 경우, 3으로 끝나는 경우)

    def pathfinder(self, target):
        if target <= len(self.sum_ways):
            # 2. Apply modulo to the final sum on return
            return sum(self.sum_ways[target-1]) % self.MOD
        
        for i in range(len(self.sum_ways), target):
            # 3. Apply modulo at each internal calculation
            ends_with_1 = (self.sum_ways[i-1][1] + self.sum_ways[i-1][2]) % self.MOD
            ends_with_2 = (self.sum_ways[i-2][0] + self.sum_ways[i-2][2]) % self.MOD
            ends_with_3 = (self.sum_ways[i-3][0] + self.sum_ways[i-3][1]) % self.MOD
            
            self.sum_ways.append((
                ends_with_1,
                ends_with_2,
                ends_with_3,
            ))
        
        # 4. Apply modulo to the final sum on return
        return sum(self.sum_ways[target-1]) % self.MOD


ott = OTT()

# Minor suggestion: Use stdin.readline for all input for consistency
N = int(stdin.readline().rstrip()) 

for _ in range(N):
    print(ott.pathfinder(int(stdin.readline().rstrip())))