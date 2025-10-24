"""
* Problem   : 1874
* Title     : 스택 수열
* Link      : https://www.acmicpc.net/problem/1874
* Category  : Data Structure > Stack
"""
n = int(input())
order = []

# 쓰읍 이거 주석으로 설명하기에 내 어휘력이 딸리는데 일단 열심히 적어볼게요

# Step 1: 일단 주어진 입력을 order에 다 받아둔다
for _ in range(n):
    order.append(int(input()))

# Step 2: 주어진 입력이 스택 수열인지 판단하기 위해 필요한 변수들
# * put_check   :: 해당하는 index의 수가 사용된 적이 있는지 확인하기 위한 list
# *             ex) put_check[3] = 1 이면, '3'은 스택 수열인지 판단하는 과정에서 사용된 적이 있다
put_check = [0 for _ in range(0,n+1)]
recent = 1

# append(), pop()의 기능이 기본적으로 구현되어있기 때문에
# 개인적으로 stack을 class로 별도로 구현하기보다는 list를 사용하는 걸 선호하는 편
# (이전에 class로 구현했던 건 연습)
stack = []

# * out         :: stack 연산한 걸 저장해두는 list (append하면 +, pop하면 -를 저장)
# * no          :: 출력 결과가 'NO'인지 확인하는 flag
out = []
no = False

# [4, 3, 6, 8, 7, 5, 2, 1]
# top <---------------> bottom
# 즉, 왼쪽부터가 stack에서 뽑은 순서

# 4가 나오려면, 그전까지의 수인 1,2,3가 stack에 들어가있어야 한다
# [1, 2, 3, 4]              | out: [+, +, +, +]
# [1, 2, 3] -> (pop) 4      | out: [+, +, +, +, -]
# 이제 3이 나오려면 바로 pop 해주면 된다
# [1, 2] -> (pop) 3         | out: [+, +, +, +, -, -]
# 6이 나오려면 그전까지의 수가 stack에 들어가있어야 하는데, 이미 4까지는 들어간 적이 있으니 5,6만 넣어주면 된다
# [1, 2, 5, 6]              | out: [+, +, +, +, -, -, +, +]
# [1, 2, 5] -> (pop) 6      | out: [+, +, +, +, -, -, +, +, -]
# 8이 나오려면 그전까지의 수가 stack에 들어가있어야 하는데, 이미 6까지는 들어간 적이 있으니 7,8만 넣어주면 된다
# [1, 2, 5, 7, 8]           | out: [+, +, +, +, -, -, +, +, -, +, +]
# [1, 2, 5, 7] -> (pop) 8   | out: [+, +, +, +, -, -, +, +, -, +, +, -]
# 이후로는 순차적으로 뽑아주면 된다
# [1, 2, 5] -> (pop) 7      | out: [+, +, +, +, -, -, +, +, -, +, +, -, -]
# [1, 2] -> (pop) 5         | out: [+, +, +, +, -, -, +, +, -, +, +, -, -, -]
# [1] -> (pop) 2            | out: [+, +, +, +, -, -, +, +, -, +, +, -, -, -, -]
# [] -> (pop) 1             | out: [+, +, +, +, -, -, +, +, -, +, +, -, -, -, -, -]

# 위와 같은 순서를 따라서 스택에 넣는데, 현재 뽑아야 하는 수가 stack의 top에 있지 않으면
# 그것은 스택 수열로 만들 수 없다는 의미가 된다 

for item in order:
    if put_check[item] == 0:
        for j in range(recent,item+1):
            put_check[j] = 1
            stack.append(j)
            out.append("+")
        stack.pop()
        out.append("-")
        recent = item + 1
        
    else:
        if stack[-1] == item:
            stack.pop()
            out.append("-")
        else:
            no = True
    
if no:
    print("NO")
else:
    for o in out:
        print(o)
    