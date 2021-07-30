#BAEKJUN 2753
#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
#첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.

year=int(input())

if year%4==0 and year%100!=0:
    print("1")
elif year%400==0:
    print("1")
else :
    print("0")
