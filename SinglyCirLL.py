
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyCirLL:
    
    def __init__(self):
        self.first = None
        self.Tail = None
        self.Count = 0
        
    def InsertFirst(self,No):
        
        newn = Node(No)
        newn.next = None
        newn.data = No
        
        if(self.first == None):
            self.first = newn
            self.Tail = self.first
            self.Tail.next = self.first
        else:
            
            newn.next = self.first
            self.first = newn
            self.Tail.next = self.first
        self.Count = self.Count + 1
        
    def InsertLast(self,No):
        
        newn = Node(No)
        newn.next = None
        newn.data = No
        
        if(self.first == None):
            self.first = newn
            self.Tail = self.first
            self.Tail.next = self.first
        elif(self.first.next == self.Tail):
            newn.next = self.Tail
            self.Tail.next = self.first
        else:
            self.Tail.next = newn
            self.Tail = newn
            self.Tail.next = self.first
        self.Count = self.Count + 1
            
    def DeleteFirst(self):
        
        if(self.first == None and self.Tail == None):
            print("Linked list is already empty....")
            return
        elif(self.first.next == self.Tail):
            self.first = None
            self.Tail = None
        else:
            self.first = self.first.next
            self.Tail.next = self.first
        self.Count = self.Count - 1    
           
    def DeleteLast(self):
        Temp = self.first
        
        if(self.first == None and self.Tail == None):
            print("Linked list is already empty....")
            return
        elif(self.first.next == self.Tail):
            self.first = None
            self.Tail = None
        else:
            while(Temp.next != self.Tail):
                Temp = Temp.next
            Temp.next = None
            self.Tail = Temp
            self.Tail.next = self.first
        
        self.Count = self.Count - 1 

                         
            
    def Display(self):
        
        Temp = self.first
        
        for i in range(1,self.Count + 1,1):
            
            print("| ",Temp.data," |-->",end='')
            Temp = Temp.next
        print("NULL")
    
    
    def CountNode(self):
        
        return self.Count    

    def InsertAtPos(self,No,iPos):
        
        newn = Node(No)
        newn.next = None
        newn.data = No
        
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
            Temp.next = newn
            self.Tail.next = self.first
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
            self.Tail.next = self.first
            self.Count = self.Count + 1
            
        
def main():
    obj = SinglyCirLL()
    obj.InsertFirst(121)
    obj.InsertFirst(121)
    obj.InsertFirst(121)
    obj.InsertFirst(121)
    obj.InsertLast(151)
    obj.InsertLast(201)
    obj.Display()
    obj.InsertAtPos(11111,5)
    obj.DeleteAtPos(5)
    obj.Display()
    obj.DeleteFirst()
    obj.DeleteLast()
    iRet = obj.CountNode()
    print("Number of Nodes are : ",iRet)
    obj.Display()
    iRet = obj.CountNode()
    print("Number of Nodes are : ",iRet)

if __name__ == "__main__":
    main()