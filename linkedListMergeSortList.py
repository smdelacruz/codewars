from linkedList import Node, Linkedlist


def mergedtheList(firstList, secondList, mlist):
    currentFirst = firstList.head
    currentSecond = secondList.head
    while True:
        if currentSecond is None:
            mlist.insertToEndList(currentFirst)
            break
        if currentFirst is None:
            mlist.insertToEndList(currentSecond)
            break
        if currentFirst.data < currentSecond.data:
            currentFirstNext = currentFirst.next
            currentFirst.next = None
            mlist.insertToEndList(currentFirst)
            currentFirst = currentFirstNext
        else: 
            currentSecondNext = currentSecond.next
            currentSecond.next = None
            mlist.insertToEndList(currentSecond)
            currentSecond = currentSecondNext
        
# 1st List
NodeOne = Node(1)
NodeFive = Node(5)
NodeThree = Node(3)
firstlinkedList = Linkedlist()
firstlinkedList.insertToEndList(NodeOne)
firstlinkedList.insertToEndList(NodeThree)
firstlinkedList.insertToEndList(NodeFive)
# second List
NodeTwo = Node(2)
NodeFour = Node(4)
NodeSix = Node(6)
secondlinkedList = Linkedlist()
secondlinkedList.insertToEndList(NodeTwo)
secondlinkedList.insertToEndList(NodeFour)
secondlinkedList.insertToEndList(NodeSix)

mlist = Linkedlist()
mergedtheList(firstlinkedList, secondlinkedList, mlist)
print("printing....")
mlist.printList()