"""
* Problem   : 9093
* Title     : 단어 뒤집기
* Link      : https://www.acmicpc.net/problem/9093
* Category  : Data Structure > Stack
"""
t = int(input())
out = []

for _ in range(t):
    sentence = input().split()
    reverse = []
    for word in sentence: # string = list of 'char's
        # 의도대로 푸는거라면.. 스택을 하나 만들어서 넣었다가 빼는거지만 
        # word[::-1] 으로 word의 reverse된 결과를 얻을 수도 있다
        reverse.append(word[::-1])
    out.append(" ".join(reverse))

for res in out:
    print(res)

# 결과를 list에 받아뒀다가 출력하는 것과, 바로바로 출력하는 것의 시스템 채점상 차이는 없지만
# 디버깅 상 편의를 위해 out에다가 결과를 받아뒀다가 나중에 한꺼번에 출력하고 있다