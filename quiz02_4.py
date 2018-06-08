# quiz02_4.py


'''
from collections import Counter
wordDict = Counter()

s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

print(type(s))
s= s.upper().replace(",","").replace(".","")


for word in s.split(): #한 문장에 들어있는 한 단어씩
    wordDict[word] += 1 

frequency_list = wordDict.keys()
 
for words in frequency_list:
    print(words, wordDict[words])


'''

#teacher do

s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""

# 데이터 정재 
s= s.replace(",","").replace(".","").replace("\n","").upper()
print(s)


summary = {}
#문자열을 자르겠습니다 
splits = s.split(" ")
print(splits)


# 중복제거 and summary 사전 count
for split in splits:
    if split in summary.keys():
        summary[split] += 1 # 똑같은 단어는 그 카운트를 올려준다. summary[split]  => 단어수 카운트값 == value 
    else :
        summary[split] = 1

for key, value in summary.items():
    print("{}:{}".format(key,value))