#BEAKJUN 2739
#N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

n=int(input())
result=1
for x in range(1,10):
    print(n,"*",x,"=",n*x)