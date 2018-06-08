#quiz01_2 -clear
'''
# 나의 풀이

# list 선언
lst = [1,2,3,4,5,6,7,8,9,10]
print("lst:",type(lst))

# list로 부터 추출
lst_slice = lst[3:7]
print("lst_slice:",lst_slice)
#reversed
lst_slice_rever=list(reversed(lst_slice))
print("lst_slice_rever",lst_slice_rever)
# reversed한 리스트를 원래 리스트에 끼워넣기
lst[3:7]=lst_slice_rever
print("lst:",lst)
'''
'''
# list의 reverse --> 그냥 reverse()는 NONE을 반환 --> reverse()는 내부값만 바뀌고 리턴값을 반환안하기 때문에
lst = lst.reverse() --> 는 none값이 나온다, 따라서 reverse()메소드를 재정의 해서 return lst를 해주면 가능

lst = [1,2,3,4,5,6,7,8,9,10]
lst=lst.reverse()
print("rever_lst:",lst)
'''
#선생님의 풀이
lst = [1,2,3,4,5,6,7,8,9,10]

slice = lst[3:7] # 인덱스에 유의
print("slice:",slice)
slice.reverse() # 순서뒤집기
lst[3:7]=slice
print("lst:",lst)
'''

