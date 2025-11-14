"""
* Problem   : 11052
* Title     : 카드 구매하기
* Link      : https://www.acmicpc.net/problem/11052
* Category  : Dynamic Programming
"""

from sys import stdin

class CardBuyer:
    def __init__(self) -> None:
        self.cards = []
        # self.max_price = 0
        self.max_price_dict = {} # key: number of cards, value: max price
        return

    def max_price(self, N:int):
        for i in range(1, N+1):
            self.max_price_helper(i)
        
        return self.max_price_dict[N]

    def max_price_helper(self, N:int):
        if (N == 1):
            self.max_price_dict[N] = self.cards[N-1][1]
            return self.cards[N-1]
        
        else:
            max_price = self.cards[N-1][1]
            for i in range(1, N//2+1):
                if(max_price < self.max_price_dict[N-i] + self.max_price_dict[i]):
                    max_price = self.max_price_dict[N-i] + self.max_price_dict[i]
            self.max_price_dict[N] = max_price
    
    def set_cards(self, cards_list):
        self.cards = cards_list[:]


N = int(stdin.readline().rstrip())
adder = CardBuyer()

cards = [(i+1, int(x)) for i, x in enumerate((stdin.readline().rstrip()).split())]

# print(cards)
adder.set_cards(cards)
print(adder.max_price(N))
