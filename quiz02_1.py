# queiz02_1.py


def func1(n):
    sum =0
    for i in range(1,n+1):
        if i % 3 ==0:
             sum+=i
    else: 
        print("1부터 {0} 까지 3의 배수의 합={1}".format(n,sum), end=" ")


while True:
    n=input("수를 입력하세요:")
    if n.isdigit()==False :
        print("정수가 아닙니다. 다시입력하세요")
    else :
        func1(int(n))
        break



'''

teacher do
'''

while True:
    num= input("수를 입력하세요")

    if num.isdigit():
        break

    print("정수가 아닙니다. 다시입력하세요")

total = 0 
to = int(num)

for i in range(1,to+1):
    if i % 3 == 0:
        total+=1

print("1부터 {}까지의 3의 배수의 합 = {}".format(to,total)) 
