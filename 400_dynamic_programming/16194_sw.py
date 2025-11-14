"""
* Problem   : 16194
* Title     : 카드 구매하기 2
* Link      : https://www.acmicpc.net/problem/16194
* Category  : Dynamic Programming
"""

from sys import stdin

class CardBuyer:
    def __init__(self) -> None:
        self.cards = []
        self.min_price_dict = {} # key: number of cards, value: max price
        return

    def min_price(self, N:int):
        for i in range(1, N+1):
            self.min_price_helper(i)
        
        return self.min_price_dict[N]

    def min_price_helper(self, N:int):
        if (N == 1):
            self.min_price_dict[N] = self.cards[N-1][1]
            return self.min_price_dict[N]
        
        else:
            min_price = self.cards[N-1][1]
            for i in range(1, N//2+1):
                if(min_price > self.min_price_dict[N-i] + self.min_price_dict[i]):
                    min_price = self.min_price_dict[N-i] + self.min_price_dict[i]
            self.min_price_dict[N] = min_price
    
    def set_cards(self, cards_list):
        self.cards = cards_list




N = int(stdin.readline().rstrip())
cb = CardBuyer()

cards = [(i+1, int(x)) for i, x in enumerate((stdin.readline().rstrip()).split())]

# print(cards)
cb.set_cards(cards)
print(cb.min_price(N))
