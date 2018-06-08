s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""


frequency = {}
s=s.upper().replace(",","").replace(".","")

for word in s.split():
    cnt =frequency.get(word,0)
    frequency[word] = cnt + 1

frequency_list = frequency.keys()
 
for words in frequency_list:
    print(words, frequency[words])