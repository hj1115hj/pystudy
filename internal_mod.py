
# sys 모듈
# 파이썬 인터프리터 관련 정보와 기능 
# argv


import sys
 
def argv_f():
    print(sys.argv)
    args = sys.argv[1:]
    print("args:", args)


#argv_f()
# 환결 관련 내용들 

def env_f():
    # 플랫폼 정보를 얻어온다 
    print(sys.platform)
    # 시스템 버전을 얻어온다 
    print(sys.version)
    # 모듈 디렉터로 확인
    print(sys.path)

#env_f()  



import random

# 0~ 1 사이의 난수 발생 
print(random.random())
# 특정 범위의 정수내에서 정수 난수 발새 ㅇ
 
print(random.randint(1,6))

# 랜덤 유틸리티 함수 

seq =["짬뽕","짜장면","짬짜면"]
# 이 리스트를 섞어 봅시다 : shuffle


random.shuffle(seq)
print(seq)

#순차형에서 임의의 한개 객체 반환 
print(random.choice(seq))


# Sampling

print(random.sample(range(1,46),6)) # 1~45 사이의 순차정수중에서 6개를 추출 

# Namespace 특정값들과 기능들을 모아서 제공한다. 
 


