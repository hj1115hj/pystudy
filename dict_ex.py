#dict_ex.py

#사전 
#순서 없고 Key-value 매칭 자료형
#len(), in, not in
 
 #사전 만들기 
 #d= dict() #빈사전 
 #print(d,type(d))

 #방법 2 " {을 이용하여 만들기}"
d = {}
print(d, type(d))

 # 방법 3 : key - value  arg를 이용하여 만들기 
d= dict(one = 1, two=2)
print(d,type(d))
 
 #방법 4: key, value 리스트 들이 따로잇을때 
 
keys = ("one","two","tree")
values = (1,2,3)
 
d= dict(zip(keys,values))
print(d,type(d))

 # 사전의 키 
print("--------key")
 #변경 불가 자료형을 사용 
d= {}

d[10] = "10"
d["baseball"] = 9
d[("kim",10)]  = "학생"

print(d,type(d))

#d(["lee",30])  = "근로자"  #Type Error


# 사전 메서드
print("-------Methods")

d = {"baseball" : 9, "soccer" : 11, "baseketball" : 5} 
print(d,type(d))

#키 목록을 가져와 보겠습니다... keys()

print(d.keys()) 

#값의 목록 : value()

print(d.values())

#키와 값의 목록 : items()

print(d.items()) 


# 값 가져오기 
print(d['baseball'])
#print(d['handball'])  key error

#값 가져오기2 : get
print(d.get('handball'))

print(d.get('handball',"?")) # 기본값을 ?


# 값의 삭제 : del 함수 
del d['soccer']

print(d)

#사전 비우기 
d.clear()
print(d)

print("------------순회") 

d['soccer'] =11

d = {"baseball" : 9, "soccer" : 11, "baseketball" : 5} 
print(d)
#방법 1 : 키 값을 순회하면서 받아와서 내용처리
for key in d:
    print(key, ":" , d[key])

for key in d.keys():
    print(key,":",d[key])

#방법 2 : 키와 값을 함께 받아와서 활용: items()
for key, value in d.items():
    print("{0}:{1}".format(key,value), end = " ")
else: 
   print()
