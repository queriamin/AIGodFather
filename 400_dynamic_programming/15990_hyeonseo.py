# 런타임 에러 RecursionError
class Number:
    def __init__(self):
        self.dict = {3: (1, 1, 0), 4:(2, 0, 1), 5:(1, 2, 1)}

    def get_number(self, n):
        if n in self.dict:
            return self.dict[n]
        one = self.get_number(n - 1)[1] + self.get_number(n - 1)[2]
        two = self.get_number(n - 2)[0] + self.get_number(n - 2)[2]
        three = self.get_number(n - 3)[0] + self.get_number(n - 3)[1]
        self.dict[n] = (one, two, three)
        return self.dict[n]

    def count_way(self, n):
        one, two, three = self.get_number(n)
        print((one + two + three) % 1000000009)

num = Number()
T = int(input())

for t in range(T):
    N = int(input())
    num.count_way(N)    