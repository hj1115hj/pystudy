
import math as m

#모듈명을 바꿔보겠습니다 : as
print(m.pi)


#모듈 내에 정의된 객체의 이름을 바꾸기
from mymod import add as sumval
print(sumval(10,20))  # mymode.add -> sumval



#dir 함수 
# 해당 객체가 어떤 변수와 메서드를 가지고있는지 확인
print(dir(m))
