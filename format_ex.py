# format_ex.py
# 문자열 서식

# 서식문자 
'''

%s : 문자열
%d : 정수
%f : 부동소수
%% : % 리터럴
'''

format ="I have %d apples"
print(format % 10)

print("Interest Rate is %f%%" % 1.24)

format = "total : %d개, get: %d개"
print(format % (10,3))

#format과 값의 형식이 일치하지 않으면 Type Error가 발생 
 
 # 고급 포매팅
format_str = "I have {} apples, ans I ate {} apples." 
print(format_str.format(5,3))

# 서식에 설정된 공간의 개수와 실제 값의 개수가 다르면 IndexError 가 발생 
print(format_str.format(10,3,1))

#print(format_str.format(10)) # index error

# 이름 기반의 포맷 
format_str = "I have {total}  apples, and I ate {num} apples."
print(format_str.format(total = 10, num = 3))

#print(format_str.format(total = 10))  # key error


# dict 객체를 이용한 초맷 
print(format_str.format_map({"total": 5, "num" : 2}))
