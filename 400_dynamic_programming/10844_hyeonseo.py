# 메모리 초과
max_N = 100

def found_child(list):
    child_list = []
    for l in list:
        if l == 0:
            child_list.append(1)
        elif l == 9:
            child_list.append(8)
        else:
            child_list.append(l - 1)
            child_list.append(l + 1)
    return child_list

count_list = [0, 9]
answer_list = [0, 9, 17] + [0 for _ in range(max_N - 2)]

for i in range(2, max_N):
    count_list = found_child(count_list)
    count = len([x for x in count_list if x != 0])
    answer_list[i + 1] = answer_list[i] * 2 - count

N = int(input())
print(answer_list[N])