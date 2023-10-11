import random

list=[10]
for i in range(10):
    list.append(random.randint(1,100))
print(list)

def bubble_sort(list):
    for j in range(len(list)):
        for i in range(len(list)-j-1):
            if list[i] > list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return list

def selected_sort(list):
    for i in range(len(list)):
        minnumber = list.index(min(list[i:]))
        list[i],list[minnumber]=list[minnumber],list[i]
    return list
    

def insert_sort(list):
    for i in range(1,len(list)):
        number = list[i]
        j=i-1
        while j>=0 and number < list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=number
    return list        
        
def heapify(list,n,root):
    point = root
    left = root*2+1
    right = root*2+2

    if left < n and list[left] > list[point]:
        point=left
    if right < n and list[right] > list[point]:
        point =right
    if root != point :
        list[point],list[root] = list[root] ,list[point]
        heapify(list,n,point)


def heap_sort(list):
    n=len(list)

    for i in range(n//2-1,-1,-1):
        heapify(list,n,i)

    for i in range(n-1,0,-1):
        list[0],list[i] = list[i],list[0]
        heapify(list,i,0)
    
    return list

def merge(x,y):
    list=[]
    i,j = 0,0
    while i < len(x) and j< len(y):
        if x[i]>y[j]:
            list.append(x[i])
            i+=1
        else:
            list.append(y[j])
            j+=1
    list.extend(x[i:])
    list.extend(y[j:])
    return list

def merge_sort(list):
    if len(list) <=1:
        return list
    
    n = len(list)//2
    x= list[:n]
    y= list[n:]

    x=merge_sort(x)
    y=merge_sort(y)

    return merge(x,y)

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    n = random.randint(0,len(list)-1)
    x= []
    mid=[]
    y= []
    for i in range(len(list)):
        if i==n:
            mid.append(list[i])
        elif list[n] > list[i]:
            x.append(list[i])
        else:
            y.append(list[i])

    x= quick_sort(x)
    y= quick_sort(y)

    sortlist = x+mid+y

    return sortlist

print(quick_sort(list))


         