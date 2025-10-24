"""
* Problem   : 1158
* Title     : 요세푸스 문제
* Link      : https://www.acmicpc.net/problem/1158
* Category  : Data Structure > Queue
"""
# 아래 코드를 python3로 제출하면 '시간초과'가 발생하지만,
# pypy3로 제출하면 맞았다고 처리된다

n,k = [int(x) for x in input().split()]

# 문제에서 시키는 대로 queue에 넣어놓고, k번째가 될 때마다 pop해주면 된다
people = [x for x in range(1, n+1)]
remove = []

# * cnt     : 현재 '몇'번째 사람을 보고 있는지 체크하는 변수
# *     ex) cnt = 3이면 3번째 사람을 체크하고 있다는 의미이다
cnt = 1
while(len(people)>0):
    top = people[0]
    if cnt%k==0: # k번째 일때마다 체크해서 pop
        remove.append(top)
        del people[0]
    else: # 그외에는 다음 순서를 봐야하므로 다시 people에 넣어준다
        people.append(top)
        del people[0]
    cnt+=1

# 출력 형식을 맞춰주기 위한 과정
answer = ", ".join([str(x) for x in remove])
answer = "<" + answer + ">"
print(answer)