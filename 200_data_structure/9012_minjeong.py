# # 명금이랑 같이 푼 거
# num_case = int(input()) # 케이스 수를 int()로 받아오기
# out = []

# for num in range(num_case):
#     pang = input()
#     res = ""
#     stack = []

#     for p in pang:
#         if p == "(":
#             stack.append(p)
#         else:
#             if len(stack) == 0:
#                 res = "NO"
#                 break
#             elif stack[-1] == "(":
#                 stack.pop()
    
#     if res == "" and len(stack) == 0:
#         res = "YES"
#     else:
#         res = "NO"
    
#     out.append(res)

# for res in out:
#     print(res)

# 한 번 더!
num_case = int(input())
out = []

for num in range(num_case):
    stack = []
    pang = input()
    res = ""

    for p in pang:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) == 0:
                res = "NO"
                break
            elif stack[-1] == "(":
                stack.pop()
    
    if res == "" and len(stack) == 0:
        res = "YES"
    else:
        res = "NO"

    out.append(res)

for res in out:
    print(res)
