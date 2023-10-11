import random

class node:
    def __init__(self,value) -> None:
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__(self) -> None:
        self.root=None
        self.size=0

    def insert(self,value):
        if self.root is None:
            self.root=node(value)
            self.size+=1
        else:
            self.insertcheck(self.root,value)

    def insertcheck(self,currentvalue,value):
        if currentvalue.value<value:
            if currentvalue.right is None:
                currentvalue.right = node(value)
                self.size+=1
            else:
                self.insertcheck(currentvalue.right,value)
        elif currentvalue.value == value:
            print("it exist")
        else:
            if currentvalue.left is None:
                currentvalue.left =node(value)
                self.size+=1
            else:
                self.insertcheck(currentvalue.left,value)



    def delete(self, currentvalue,value):
        if currentvalue is None:
            return None

        elif currentvalue.value < value:
            currentvalue.right = self.delete(currentvalue.right,value)
        elif currentvalue.value > value:
            currentvalue.left = self.delete(currentvalue.left,value)
        elif currentvalue.value == value:
            
            if currentvalue.left is None:
                self.size-=1
                return currentvalue.right
            elif currentvalue.right is None:
                self.size-=1
                return currentvalue.left

            replacenode = self.findmaxnode(currentvalue.left)
            currentvalue.value = replacenode.value
            currentvalue.left = self.delete(currentvalue.left,replacenode.value)
            self.size-=1
        return currentvalue

    def deletenode(self,value):
        if self.root is None:
            print("tree is empty")
        else:
            self.delete(self.root,value)

    def findmaxnode(self,node):
        while node.right:
            node = node.right
        return node
    

binarytree = Tree()
for i in range(10):
    binarytree.insert(i)
    print(binarytree.size)

binarytree.deletenode(5)
print(binarytree.size)
    
            
            
            


        
             
            
    
    

            
