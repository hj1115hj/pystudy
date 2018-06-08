
from math import pi, sin, cos, tan
from mymod import pi,add,subtract, multiply

# 모듈명 지정없이 이름으로만 호출할수 있게 
print(pi)

print(add(10,20))

# 객체 내부에 __module__ 을 확인하면 그 객체가 어느 모듈에 속해있는지 확인 
# add  메서드의 모듈은 무엇인가 

print(add.__module__)
print(dir(add.__module__))  # add메서드의 객체의 내부 변수와 객체의 목록


# add객체의 모듈에 있는 subtract 함수를 실해해 봅시다 
# eval


# add객체의 모듈에 있는 subtract 함수를 실행해 봅시다 
# eval: 문자열로 넘겨받은 배용에 대해 실행을 시도 

print(eval(add.__module__+".subtract(10,10)"))
