class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
        self.tail = None
    def printAllVals(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
    def addBack(self, val):
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = SLNode(val)
        self.tail = runner.next
        print("addBack: " + runner.value)
    def addFront(self, val):
        temp = self.head
        self.head = SLNode(val)
        self.head.next = temp
        print("addFront: " + self.head.value)
    def insertBefore(self, nextVal, val):
        runner = self.head
        while(runner.next != None):
            if(runner.next.value == nextVal):
                temp = runner.next
                runner.next = SLNode(val)
                runner.next.next = temp
                break
            runner = runner.next
    def insertAfter(self, preval, val):
        runner = self.head
        while(runner.next != None):
            if(runner.value == preval):
                temp = runner.next
                runner.next = SLNode(val)
                runner.next.next = temp
                break
            runner = runner.next
    def removeNode(self, val):
        runner = self.head
        while(runner.next != None):
            if(runner.next.value == val):
                runner.next = runner.next.next
                break
            runner = runner.next
    def reverseList(self):
        curr = self.head
        pre = None
        while(curr != None):
            temp = curr.next # Save next object
            curr.next = pre # Reverse pointer
            pre = curr # Advance pre
            curr = temp # Advance curr
        self.head = pre

list = SList()
list.head = SLNode('Alice')
list.head.next = SLNode('Chad')
list.head.next.next = SLNode('Debra')
#list.printAllVals()
list.addBack('Esther')
list.addFront('Beatrice')
list.insertBefore('Chad', 'Mary')
list.insertAfter('Debra', 'Jeff')
list.removeNode('Mary')
list.reverseList()
list.printAllVals()
