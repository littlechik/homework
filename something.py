import random
"""euclidean"""
def euclidean(x,y):
    while y!=0:
       x,y = y, x%y
    print(x)
euclidean(100,10)

"""primality"""
def primality(x):
    list=[]
    for i in range(5):
        list.append(random.randint(0,x-1))
        if (list[i]**x)%x != list[i]:
            print("false")
            break
primality(121)

"""hanoi"""
def haoni(x,begin,target,middle):
    if x>0:
        haoni(x-1,begin,middle,target)
        print(str(x)+"from"+str(begin) +"move to"+str(target))
        haoni(x-1,middle,target,begin)


    