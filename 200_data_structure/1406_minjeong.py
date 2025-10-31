# 세팅
txt = list(input())
num_case = int(input())
cursor = len(txt)
# print(cursor)

for n in range(num_case):
    work = input()
    if work == "L":
        if cursor == 0:
            pass
        else:
            cursor -= 1
    elif work == "D":
        if cursor == len(txt):
            pass
        else:
            cursor += 1 
    elif work == "B":
        if cursor == 0:
            pass
        else:
            del txt[cursor-1]
    else:
        print("add")

print(txt)