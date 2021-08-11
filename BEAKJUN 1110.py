#BEAKJUN 10951
#첫째 줄에 N의 사이클 길이를 출력한다


n=int(input())
k=n

x=n//10
y=n%10
print(x,y)

n = x + y
cycle=1
print(n)

x = n //10
y =n%10
n = 10 * y + n % 10

print(n)
'''
while True:


    x=n%10
    y=n-10*x
    n=10*y+(x+y)%10
    cycle=cycle+1

    if n==k:
        break

print(cycle)
'''