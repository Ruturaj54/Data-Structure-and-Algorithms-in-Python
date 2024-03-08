
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.Count = 0
    
    def Push(self,No):
        newn = Node(No)
        newn.next = None
        newn.data = No
        
        if(self.first == None):
            self.first = newn
            newn.next = None
        else:
            newn.next = self.first
            self.first = newn
        self.Count = self.Count + 1
        
        
    def POP(self):
        Value = 0
        if(self.first == None):
            print("There is No element to Pop...")
            print("Stack is Empty..")
            return
        elif(self.first.next == None):
            Value = self.first.data
            self.first = None
        else:
            Value = self.first.data
            self.first = self.first.next
        self.Count = self.Count + 1
        return Value   
            
    
            
        
    def Display(self):
        
        Temp = self.first
        print("Contents of stack are : ")
        print("_________")
        while(Temp != None):
            print("|",Temp.data,"|")
            Temp = Temp.next
        print("_________")
    
    def CountNode(self):
        
        return self.Count
    
    

def main():
    obj = Stack()
    obj.Push(111)
    obj.Push(121)
    obj.Push(151)
    obj.Push(201)
    obj.Push(211)
    obj.Display()
    iRet = obj.CountNode()
    print("Number of nodes are : ",iRet)
    
    iRet = obj.POP()
    print("poped element is : ",iRet)

if __name__=="__main__":
    main()