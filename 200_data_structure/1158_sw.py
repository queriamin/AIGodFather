"""
* Problem   : 1158
* Title     : 요세푸스 문제
* Link      : https://www.acmicpc.net/problem/1158
* Category  : Data Structure > Queue
"""

from collections import deque

def josephus(len_lst, k):
    roster = list(range(1,len_lst+1))
    killed = deque()
    
    gun = -1
    while roster:
        gun += k 
        gun = gun % len(roster)
        killed.append(roster.pop(gun % len(roster)))
        gun -= 1
    print("<" + ", ".join([str(x) for x in killed])+ ">")

i = input()
s = i.split()
josephus(int(s[0]), int(s[1]))
