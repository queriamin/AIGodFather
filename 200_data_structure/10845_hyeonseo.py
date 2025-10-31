import sys
input = sys.stdin.readline

queue = []

N = int(input())

for i in range(N):
    s = input().split()
    command = s[0]

    if command == "push":
        queue.append(s[1])
    elif command == "pop":
        print(queue.pop(0) if queue else -1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        print(0 if queue else 1)
    elif command == "front":
        print(queue[0] if queue else -1)
    elif command == "back":
        print(queue[-1] if queue else -1)
    else:
        pass