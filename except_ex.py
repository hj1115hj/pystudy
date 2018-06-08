def try_f1():
    try:
        lst =[1,3,5,7,9]
        lst[5]
    except:
        print("Error")


#try_f1()

def try_f2():
    try:
        value = int("10a") #ValueError
    except ValueError as e: # 특정 상황에 있는 오류들을 위로 올려서 처리하고
        print("반환할수 없습니다.")
    except Exception as e: #맨마지막에 Excption 을 명시해서 예상하지 못한 오류를 잡는다
        print("Exception e:",e)
        print("type e:" ,type(e))

#try_f2()


def try_f3():
    result = 4/0 # ZeroDivisionError

#try_f3()

def example():
    num1 = input("첫번째 숫자를 입력해 주세요:")
    num2 = input("두번째 숫자를 입력해 주세요:")

    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 /num2
    except ValueError  as e:
        print("정수형이 아니에요.:")
    except ZeroDivisionError as e:
        print("0으로는 나눌수 없어요:.")

    except Exception as e:
        print("e:", e)

    else : # 오류가 없을때만 실행
        print("{}/{} = {}".format(num1,num2,result))
    finally : # 오류 여부 상관없이 마지막에 실행
        print("예외처리 완료")

#example()

# 특정 경우에는 일부러 예외를 발생시키기도 합니다 

def beward_dog(animal):
    if animal == "dog":
        #예외발생
        raise RuntimeError("멍멍")
    else:
        print("어서오세요")


try:
    beward_dog("cow")
    beward_dog("cat")
    beward_dog("dog")
except RuntimeError as e:
    print(e)
    print(type(e))



