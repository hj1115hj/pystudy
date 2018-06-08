# quiz02_3.py

'''
def summary(* args):
    sum=0
    min=100000
    max=0
    avg=0
    for i in args:
        if max<i:
            max = i
        if min>i:
            min = i 
        sum+=i
    else : avg=sum/len(args)
    return (sum,max,min,avg)
 


total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)

'''

def summary(*args):
    data = []
    total = 0
    for arg in args:
        if isinstance(arg, (int,float)):
            data.append(arg)
            total += arg

    return total,max(data),min(data),total/len(data) 


total, maxval, minval, avg = summary(80, 75, 90, 95, 85)
print(total, maxval, minval, avg)