a, b, c = map(int, input().split()) # 정수 매핑하는 함수
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)