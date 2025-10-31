import sys
input = sys.stdin.readline

N = int(input())
num_list = list(range(1, N + 1))
stack = []
result = []
possible = True

for n in range(N):
    target = int(input())
    while stack or num_list:
        if not stack:
            for t in range(target):
                stack.append(num_list.pop(0))
                result.append('+')
            stack.pop()
            result.append('-')
            break
        elif stack[-1] == target:
            stack.pop()
            result.append('-')
            break
        elif stack[-1] < target:
            while stack and stack[-1] < target:
                stack.append(num_list.pop(0))
                result.append('+')
            stack.pop()
            result.append('-')
            break
        else:
            possible = False
            break

if possible:
    print('\n'.join(result))
else:
    print('NO')