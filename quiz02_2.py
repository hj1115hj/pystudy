# quiz02_2.py

def isNumber(s):
  
  try:
    n = float(s)
    return n
  except ValueError:
    return False

lst = [1, 3.14, 'python', 7, 89.1, 3]

lst_cleaned = []
for i in lst:
    n = isNumber(i)
    if n!=False:
      lst_cleaned.append(n)
else:
    print(lst_cleaned)


  #teacher do

lst = [1,3.14,'python',7,89.1,3]

lst_cleaned = []

for item in lst:
  #if isinstance(item,int)  pr isinstance(item,float):
  if isinstance(item,(int,float)): # 안쪽에 있는것중이 하나만 만족하면됨
    lst_cleaned.append(item)

print(lst_cleaned)