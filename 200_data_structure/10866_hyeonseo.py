import sys
input = sys.stdin.readline
N = int(input())
deque = []

for i in range(N):
    s = input().split()

    if len(s) == 2:
        if s[0] == "push_front":
            deque.insert(0, s[1])
        elif s[0] == "push_back":
            deque.append(s[1])
    elif len(s) == 1:
        if s[0] == "pop_front":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.pop(0))
        elif s[0] == "pop_back":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.pop())
        elif s[0] == "size":
            print(len(deque))
        elif s[0] == "empty":
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        elif s[0] == "front":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[0])
        elif s[0] == "back":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[-1])