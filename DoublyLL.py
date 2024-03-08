
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLL:
    
    def __init__(self):
        
        self.first = None
        self.Count = 0
    
    def InsertFirst(self,No):
        
        newn = Node(No)
        newn.data = No
        newn.next = None
        newn.prev = None
        
        if(self.first == None):
            
            self.first = newn
            self.first.next = None
            self.first.prev = None
            
        else:
            
            newn.next = self.first
            self.first.prev = newn
            self.first = newn
            
        self.Count = self.Count + 1
            
     
    def InsertLast(self,No):
        
        newn = Node(No)    
        newn.data = No
        newn.next = None
        newn.prev = None
        Temp = self.first
        
        if(self.first == None):
            self.first = newn
            newn.next = None
            newn.prev = None
        elif(self.first.next == None):
            self.first.next = newn
            newn.prev = self.first
            newn.next = None
        else:
            while(Temp.next != None):
                Temp = Temp.next
            
            Temp.next = newn
            newn.prev = Temp
            newn.next = None
            
        self.Count = self.Count + 1
    
    def DeleteFirst(self):
        
        if(self.first == None):
            print("Linked list is already Empty...")
            return
        elif(self.first.next == None):
            self.first.prev = None
            self.first = None
        else:
            self.first = self.first.next
            self.first.prev = None
        
        self.Count = self.Count - 1
    
    
    def DeleteLast(self):
        Temp = self.first
        
        if(self.first == None):
            print("Linked list is already empty...")
            return
        elif(self.first.next == None):
            self.first = None
        else:
            
            while(Temp.next.next != None):
                Temp = Temp.next
            
            Temp.next = None
        
        self.Count = self.Count - 1
        
           
           
    def Display(self):
        
        Temp = self.first
        
        print("NULL <==>",end = '')
        while(Temp != None):
            print("| ",Temp.data," |<==>",end='')
            Temp = Temp.next
        print("NULL")
    
        
    def CountNode(self):
        
        return self.Count

    def InsertAtPos(self,No,iPos):
        
        newn = Node(No)
        newn.data = No
        newn.next = None
        newn.prev = None
        Temp = self.first
        
        if(iPos < 1 and iPos > self.Count + 1):
            print("Invalid Position..")
            return
        elif(iPos == 1):
            self.InsertFirst(No)
        elif(iPos == self.Count):
            self.InsertLast(No)
        else:
            for i in range(1,iPos - 1,1):
                Temp = Temp.next
            
            newn.next = Temp.next
            newn.prev = Temp
            Temp.next = newn
            
        self.Count = self.Count + 1
    
    def DeleteAtPos(self,iPos):
        
        Temp = self.first
        
        if(iPos < 1 and iPos > self.Count):
            print("Invalid Position..")
            return
        elif(iPos == 1):
            self.DeleteFirst()
        elif(iPos == self.Count):
            self.DeleteLast()
        else:
            for i in range(1,iPos-1,1):
                Temp = Temp.next
            
            Temp.next = Temp.next.next
            Temp.next.prev = Temp
        
        self.Count = self.Count - 1
            
            
                   
def main():
    
    obj = DoublyLL()
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
    
    # obj.InsertAtPos(1111,4)
    
    # obj.Display()
    # iRet = obj.CountNode()
    # print("Number of Nodes are : ",iRet)
    # obj.DeleteFirst()
    # obj.DeleteLast()
    # obj.Display()
    # iRet = obj.CountNode()
    # print("Number of Nodes are : ",iRet)
    
    # obj.DeleteAtPos(4)
    
    obj.Display()
    iRet = obj.CountNode()
    print("Number of Nodes are : ",iRet)
    
    # obj.DeleteFirst()
    # obj.Display()

if __name__ == "__main__":
    main()