# Q1_1 - clear
'''
#나의 풀이
str1 = "Life is too short, You need Python"
# 소문자로 변경 , 공백, ',' 제거
str2= str1.lower().replace(" ","").replace(",","")
print("str2:",str2)

#형변환
lst = list(str2)
print("lst:",lst)

# chars변수 -- set우로 형변환
chars = set(lst)
print(type(chars))
print("chars:",chars)

# 다시 list로 형변환
lst = list(chars)
print("lst:",type(lst))
print("lst:",lst)

# 알파벳 순으로 정렬
sort_lst= sorted(lst)
print("sort_lst:",sort_lst)

# 길이 출력
length = len(sort_lst)
print("length:",length)
'''
# 선생님 풀이

str = "Life is too short, You need Python"

str = str.lower() # 다 소문자로 변환
str = str.replace(" ","") # 공백제거
str = str.replace(",","") # 쉼표제거
#형변환
lst = list(str)
print("lst:",lst)
#set으로 형변환
chars = set(lst)
print("chars:",chars)
#다시 list로 형변환
lst = list(chars) # 왜냐하면 set은 중복을 없애고 순서가 뒤죽박죽 , 중복없애는게 주목적
print("lst:",lst)

# sort
lst.sort()
print("lst:",lst)
print("length of list:",len(lst))




