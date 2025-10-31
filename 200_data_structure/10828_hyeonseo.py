import sys
input = sys.stdin.readline

stack = []

N = int(input())

for i in range(N):
    s = input().split()
    command = s[0]

    if command == "push":
        stack.append(s[1])
    elif command == "pop":
        print(stack.pop() if stack else -1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        print(stack[-1] if stack else -1)
    else:
        pass