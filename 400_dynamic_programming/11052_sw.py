"""
* Problem   : 11052
* Title     : 카드 구매하기
* Link      : https://www.acmicpc.net/problem/11052
* Category  : Dynamic Programming
"""

from sys import stdin

# class CardBuyer:
#     def __init__(self) -> None:
#         self.cards = []
#         self.max_price = 0
#         return

#     def flex(self, target):
#         for n, p in self.cards:
#             self.flex_helper(target, n, p, n)
#         return self.max_price

#     def flex_helper(self, target, card_num, price, last_pack_size):
#         if(card_num == target and price > self.max_price):
#             self.max_price = price
#             return

#         for i in range(last_pack_size-1, len(self.cards)+1):
#             n = self.cards[i][0]
#             p = self.cards[i][1]
#             if(card_num + n > target):
#                 break
#             self.flex_helper(target, card_num+n, price+p, n)
#         return
    
#     def set_cards(self, cards_list):
#         self.cards = cards_list


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
        self.cards = cards_list


N = int(stdin.readline().rstrip())
adder = CardBuyer()

cards = [(i+1, int(x)) for i, x in enumerate((stdin.readline().rstrip()).split())]

# print(cards)
adder.set_cards(cards)
print(adder.max_price(N))
