num_case = int(input())

for num in range(num_case):
    sentence = input().split()
    for word in sentence:
        flip = []
        res = ""
        for c in word:
            flip.append(c)
        for f in range(len(word)):
            # print(flip.pop(), end="")
            res += flip.pop()
        print(res, end=" ")
    print()
        