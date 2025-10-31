import sys
input = sys.stdin.readline
sentence = str(input())
N = int(input())
curser = len(sentence)

for i in range(N):
    order = str(input().strip())
    if order == "L":
        if curser != 0:
            curser -= 1
    elif order == "D":
        if curser != len(sentence):
            curser += 1
    elif order == "B":
        if curser != 0:
            sentence = sentence[:curser-1] + sentence[curser:]
            curser -= 1
    else:
        char = order.split(" ")[1]
        sentence = sentence[:curser] + char + sentence[curser:]
        curser += 1
print(sentence)