"""
* Problem   : 9093
* Title     : 단어 뒤집기
* Link      : https://www.acmicpc.net/problem/9093
* Category  : Data Structure > Stack
"""

from sys import stdin

def reverse_word(s: str):
	tokens = s.split()
	result_tokens = []
	for token in tokens:
		rev = ""
		for i in range(len(token) - 1, -1, -1):
			rev += token[i]
		result_tokens.append(rev)
	print(" ".join(result_tokens))


N = int(input())

for _ in range(N):
    reverse_word(stdin.readline().rstrip())
