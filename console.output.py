#print 함수 안에 출력할 내용을 인자값을 전달
print(2018) 
print(3.14123)
print("hello Python")

#여러 내용의 연속 출력: ,로연결
print("Hello", "python")

#문자열을 합쳐서 출력 : + 로 연결
print("Hello" + " " +"python")

#문자열 반복 출력: * 사용
print("python" * 3)

# 문자열과 다른 형식을 + 했을 경우 : type error
# print(3+"python")

# solution : casting을 시도한다
print(str(3)+"python")

# 구분자 :sep 와 end 변경
print("정인영","강의중",sep=":",end="") # :으로 구분, 개행안함
print("추가문자열")
