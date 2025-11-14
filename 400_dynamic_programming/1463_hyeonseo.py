# 틀렸습니다
import math

X = int(input())

if X >= 3:
    cal = 0
    max2n = 2
    max3n = 3

    while True:
        if max2n <= X:
            max2n *= 2
        else:
            max2n /= 2
            break

    while True:
        if max3n <= X:
            max3n *= 3
        else:
            max3n /= 3
            break

    print(f'{max2n}, {max3n}')

    if X - max2n >= X - max3n:
        cal += X - max3n
        cal += math.log(max3n, 3)
    else:
        cal += X - max2n
        cal += math.log(max2n, 2)

    print(int(cal))
elif X == 2:
    print(1)
else:
    print(0)