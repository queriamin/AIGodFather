import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    sentence = str(input())
    stack = []
    not_vps = False
    for s in sentence:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                not_vps = True
                break
    if not_vps or stack:
        print("NO")
    else:
        print("YES")