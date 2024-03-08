
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCirLL:
    
    def __init__(self):
        self.first = None
        self.Tail = None
        self.Count = 0
    
    def InsertFirst(self,No):
        
        newn = Node(No)
        newn.data = No
        newn.next = None
        newn.prev = None
        
        if(self.first == None and self.Tail == None):

            self.first = newn
            self.Tail = newn
            newn.next = self.Tail
            newn.prev = self.first
               
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn
            
        self.Tail.next = self.first    
        self.first.prev = self.Tail
        self.Count = self.Count + 1
        
    
    def InsertLast(self,No):
                
        newn = Node(No)
        newn.data = No
        newn.next = None
        newn.prev = None
        
        if(self.first == None and self.Tail == None):
            self.first = newn
            self.Tail = newn
            newn.next = self.Tail
            newn.prev = self.first
              
        else:
            self.Tail.next = newn
            newn.prev = self.Tail
            self.Tail = newn
            
            
        self.Tail.next = self.first
        self.first.prev = self.Tail
        self.Count = self.Count + 1
        
      
    def DeleteFirst(self):
        
        if(self.first == None and self.Tail == None):
            self.first = None
            self.Tail = None      
        else:       
            self.first = self.first.next
            self.first.prev = self.Tail
            self.Tail.next = self.first
        
        self.Count = self.Count - 1
        
    
    def DeleteLast(self):
        
        if(self.first == None and self.Tail == None):
            self.first = None
            self.Tail = None      
        else:       
            self.Tail = self.Tail.prev
            
        self.Tail.next = self.first
        self.first.prev = self.Tail
        self.Count = self.Count - 1
        
           
    def Display(self):
        
        Temp = self.first  
        print("To Tail<==>",end = '')
        for i in range(1,self.Count + 1,1):
            print("| ",Temp.data," |<==>",end='')
            Temp = Temp.next
        print("To Head")
    
        
    def CountNode(self):
        
        return self.Count

    def InsertAtPos(self,No,iPos):
        newn = Node(No)
        newn.data = No
        newn.next = None
        newn.prev = None
        
        if(iPos < 1 and iPos > self.Count + 1):
            print("Invalid Position...")
            return
        elif(iPos == 1):
            self.InsertFirst(No)
        elif(iPos == self.Count):
            self.InsertLast(No)
        else:
            
            Temp = self.first
            
            for i in range(1,iPos - 1,1):
                Temp = Temp.next
            
            newn.next = Temp.next
            Temp.next.prev = newn
            Temp.next = newn
            newn.prev = Temp
            
        self.Tail.next = self.first
        self.first.prev = self.Tail
        self.Count = self.Count + 1  
    
    def DeleteAtPos(self,iPos):
        
        if(iPos < 1 and iPos > self.Count):
            print("Invalid Position...")
            return
        elif(iPos == 1):
            self.DeleteFirst()
        elif(iPos == self.Count):
            self.DeleteLast()
        else:
            
            Temp = self.first
            for i in range(1,iPos - 1,1):
                Temp = Temp.next
            
            Temp.next = Temp.next.next
            Temp.next.prev = Temp
            
        self.Tail.next = self.first
        self.first.prev = self.Tail
        self.Count = self.Count - 1    
            

def main():
    
    obj = DoublyCirLL()
    obj.InsertFirst(101)
    obj.InsertFirst(111)
    obj.InsertFirst(121)
    obj.InsertFirst(151)
    obj.InsertLast(1001)
    obj.InsertLast(111)
    obj.InsertLast(121)
    obj.InsertLast(151)
    obj.InsertAtPos(11111,4)
    
    obj.DeleteAtPos(4)

    obj.Display()
    iRet = obj.CountNode()
    print("Number of Nodes are : ",iRet)
    
    # obj.DeleteFirst()
    # obj.Display()

if __name__ == "__main__":
    main()
            
            
            
            
            
            
        
        
