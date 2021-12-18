class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def checkList(self):
        counter = 0
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            currentNode = currentNode.next
            counter += 1
        return counter

    def isListEmpty(self):
        return True if self.head is None else False

    def insertToHeadList(self, newNode):
        tempNode = self.head #Me
        self.head = newNode #[laptop] -->
        self.head.next = tempNode  #[laptop] --> Me

    def insertAtPosition(self, newNode, nodeposition):
        if nodeposition < 0 or nodeposition > self.checkList():
            print("Invalid input position")
            return

        if nodeposition == 0:
            self.insertToHeadList(newNode)
            return

        currentNode = self.head # traverse on the list
        currentPosition = 0
        while True:
            if currentPosition == nodeposition:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertToEndList(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def deleteHeadofList(self):
        """
        my solution
        """
        currentHead = self.head
        self.head = currentHead.next
        

    def deleteEndofList(self):
        """
        my solution
        """
        # curentNode = self.head
        # while True:
        #     if curentNode.next is None:
        #         previousNode.next = None
        #         break
        #     previousNode = curentNode
        #     curentNode = curentNode.next
        """
        tutorial solution
        """
        curentNode = self.head
        while curentNode.next is not None:
            previousNode = curentNode
            curentNode = curentNode.next
        previousNode.next = None


    def deleteAtPosition(self, position):
        """
        my solution
        """
        if self.isListEmpty(): 
            print("List is empty") 
            return

        if position < 0 or position >= self.checkList():
            print("Invalid input position")
            return
        
        currentNode = self.head # traverse on the list laptop 0, me 1
        currentPosition = 0
        while currentPosition != position:
            previousNode = currentNode #laptop
            currentNode = currentNode.next #me
            currentPosition += 1
        previousNode.next = currentNode.next

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node(1)
linkedList = Linkedlist()
linkedList.insertToEndList(firstNode) #Me
secondNode = Node(2)
linkedList.insertToEndList(secondNode) #coffee
thirdNode = Node(3)
linkedList.insertToEndList(thirdNode) #laptop
fourthNode = Node(4)
linkedList.insertToEndList(fourthNode)
# # linkedList.deleteEndofList()
# # forEndNode = Node("add at the end")
# # linkedList.insertToEndList(forEndNode)
# # linkedList.printList()
# # linkedList.deleteEndofList()
# linkedList.deleteAtPosition(1)
# fourthNode = Node("keyboard")
# linkedList.insertAtPosition(fourthNode, 0)
# linkedList.deleteAtPosition(10)
# linkedList.deleteHeadofList()
# linkedList.deleteHeadofList()
# linkedList.deleteEndofList()
# print(linkedList.isListEmpty())
linkedList.printList()
