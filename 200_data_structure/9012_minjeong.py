num_case = int(input())
out = []

for num in range(num_case):
    pang = input()
    res = ""

    stack = []

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