
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.Count = 0
    
    def Enqueue(self,No):
        newn = Node(No)
        newn.next = None
        newn.data = No
        Temp = self.first
        
        if(self.first == None):
            self.first = newn
            newn.next = None
        else:
            while(Temp.next != None):
                Temp = Temp.next
            
            Temp.next = newn
            newn.next = None
        self.Count = self.Count + 1
        
        
    def Dequeue(self):
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
        print("To Exit<--",end='')
        while(Temp != None):
            print("|",Temp.data,"|<--",end='')
            Temp = Temp.next
        print("<-- To Enqueue",end='')
        print()
    
    def CountNode(self):
        
        return self.Count
    
    

def main():
    obj = Queue()
    obj.Enqueue(111)
    obj.Enqueue(121)
    obj.Enqueue(151)
    obj.Enqueue(201)
    obj.Enqueue(211)
    obj.Display()
    iRet = obj.CountNode()
    print("Number of nodes are : ",iRet)
    
    iRet = obj.Dequeue()
    print("Dequeud element is : ",iRet)

if __name__=="__main__":
    main()