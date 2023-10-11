import random

"""製undirected graph"""
list=[[0]*5 for i in range(5)]

for i in range(5):
    for j in range(i+1,5):
        if random.random()>0.5:
            list[i][j]=random.randint(1,100)
            list[j][i]=random.randint(1,100)
for row in list:
    print(row)

fina =[]
for row in list:
    linklist=[i for i in range(5) if row[i]>0]
    fina.append(linklist)
print(fina)

"""路徑加權"""
fina2=[]
for row in list:
    link={i:row[i] for i in range(5) if row[i]>0}
    fina2.append(link)

print(fina2)

route=[]
"""深度查詢"""
def depthsearch(i):
    if i not in route:
        route.append(i)
        for j in fina[i]:
            depthsearch(j)
depthsearch(0)
print(route)

def stackdepth(i):
    visted=[]
    result=[]
    stack=[]
    stack.append(i)
    visted.append(i)
    while len(stack)>0:
        point = stack.pop()
        result.append(point)
        for j in fina[point]:
            if j not in visted:
                visted.append(j)
                stack.append(j)
    return result

breath=[]
"""廣度查詢"""
def breathsearch(i):
    if len(i)<1 :
        return
    node = i.pop(0)
    breath.append(node)
    for j in fina[node]:
        if j not in i and j not in breath:
            i.append(j)
    breathsearch(i)

breathsearch([0])
print(breath)

def queuebreath(i):
    visted=[]
    result=[]
    queue=[]
    visted.append(i)
    queue.append(i)
    while len(queue)>0:
        point = queue.pop(0)
        result.append(point)
        for j in fina[point]:
            if j not in visted:
                visted.append(j)
                queue.append(j)
    return result

print(queuebreath(0))


def bellman(start):
    v = len(fina2)
    distance = {node : float("inf") for node in range(v)}
    distance[start]=0
    route=[-1]*v

    for _ in range(v-1):
        for node in range(v):
            for i,weight in fina2[node].items():
                if distance[node] != float("inf") and distance[node]+weight < distance[i]:
                    distance[i] = distance[node]+weight
                    route[i]=node
    
    for a, b in distance.items():
        print(a,b)
    for n in range(v):
        point = route[n]
        list=[]
        while point !=-1:
            list.append(point)
            point=route[point]
        list.insert(0,n)
        print(list)

bellman(0)

def dijkstra(start):
    v=len(fina2)
    distance={node:float("inf") for node in range(v)}
    distance[start]=0
    route=[-1]*v
    queue=[x for x in range(v)]

    while queue:
        mindistance=float("inf")
        point=None
        for node in queue:
            if distance[node] < mindistance:
                mindistance=distance[node]
                point=node
        if point is None:
            break
        queue.remove(point)

        for i , weight in fina2[point].items():
            if distance[point]+weight< distance[i]:
                distance[i]=distance[point]+weight
                route[i]=point

    for a, b in distance.items():
        print(a,b)
    for n in range(v):
        point = route[n]
        list=[]
        while point !=-1:
            list.append(point)
            point=route[point]
        list.insert(0,n)
        print(list)

dijkstra(0)








    

    
    
