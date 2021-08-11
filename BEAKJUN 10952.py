#BEAKJUN 10952
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


a=1
b=1
while a!=0 and b!=0:
    a, b = map(int, input().split())
    if a!=0 and b!=0:
        print(a+b)
