#func_ex.py
#함수에 관한 코드 
 
def dummy():
     pass # 구현은 나중에 => 파이썬아 내부블록을 못찾기 때문에 
    
def print_hello():
    print("Hellow Python")

def times(a,b):
    return a* b

def do_nothing():
    return 

#함수의 호출

dummy() # 리턴 값이 없는 경우 
print_hello()
print(times(10,10))
print(do_nothing())


# 여러 개의 값을 반환 
def swqp(a,b):
    return b,a

s  = swqp(3,4)
print("s:",s)

s1, s2= swqp(3,4)
print("s1:", s1,"s2:",s2)

# 함수의 인자 전달 
print("---------------- args")
def func1(t):  # 가정상 t로  list가 넘어올 것을 기대 : 넘어온 인자값이 변경가는 객체인 list 이므로 문제가 없다.
    t[0] *= 2

a = [1,2,3]
func1(a)
print("a : ",a)

# immutable를 넘겼을 때는 오류가 발생할것 
#func1((1,2,3)) # TypeError

# 함수의 개선
def func2(t):
    if isinstance(t,list):
        t[0]*=2
        return True
    else:
        return False

result = func2(a)
print(result,a)

result = func2((1,2,3))
print(result)

def func3(t):
    a=30
    print("a:",a)

# 함수의 개선
'''
print("------------------")
def func2(t):
    if isinstance(t,list):
        t[0]*=2
        
        def func3(t):
            a=30
            print("a:",a)
        
        print("func2:",a)
        func3(t)
        return True
    else:
        return False



result = func2(a)
print(result,a)
'''


# 함수의 인수는 필요한 개수만큼 만들수 있다 
# 기본값을 미리 선언해 둘수 잇다 

def incr(a,step = 1) : # 두번째 인자를 넘기지 않으면 1값이 기본으로 사용된다   
    return a + step

a= 10

print(incr(a)) # step은 기본값 1로 사용 
print(incr(a,3)) # step 값은 3


#가변인수 
# 정해지지 않은 개수의 인수값을 받아 사용할때 : *
def get_total(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(get_total(1,3,5,7,9,2,4,6,8,10))


# 사전 키워드 전달: ** 
def f(a,b,*args,**kwd):
    print(a,b)
    print(args)
    print(kwd)

print(f(10,20))
print(f(10,20,30,40)) #a,b, args
print(f(10,20,30,40,option=1, option2= 2))  # option1, option2 키워드 인수

# 함수도 객체다 
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print(plus(10,20))
print(minus(30,40))

def apply(a,b, *funcs):
    for func in funcs:
        #if isinstance(func, function):
        print(func.__name__,func(a,b))


apply(1,2,plus,minus)


# 익명함수 (lambda)
def apply2(a,b,func = plus):
    return func(a,b)

print(apply2(2,3))  #  func = plus
print(apply2(2,3,multiply))  # func = multiply

print(apply2(2,3,lambda a,b: a+b))
print(apply2(2,3,lambda a,b: 2* a+b))


# 람다를 이용한 정렬 
# 리스트등 시퀀스 자료형을 정렬할때  key

strings =["Hello","Word","Python","Java"] # 정렬은 알파벳순
strings.sort()
print(strings)

strings.sort(key = lambda x : len(x))
print(strings)

