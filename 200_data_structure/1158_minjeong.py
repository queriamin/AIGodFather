input = input().split()
num_case = int(input[0])
num_remove = int(input[1])

game = list(range(1, num_case+1))
result = []
kill = -1
dead = 0

for num in range(num_case):
    if kill >= len(game):
        kill -= len(game)
        dead = game.pop()
        kill += num_remove
    else:
        dead = game.pop()
        kill += num_remove
    result.append(dead)

print(result)