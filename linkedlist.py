#singly linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating nodes

    #data part of nodes

node1 = Node(3)
node2 = Node(5)
node3 = Node(8)
node4 = Node(10)
node5 = Node(4)

    #next part of nodes

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#traverse through linked list

def traverseLinkedList(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" ")
        currentNode = currentNode.next

#deleting node from linked list(this function will return head of new linked list)

def deleteNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next
    if currentNode == None:
        return head
    currentNode.next = currentNode.next.next

    return head
        
#inserting node in linked list using position

def insertInLinkedList(head, nodeToInsert, position):
    if position == 1 :
        nodeToInsert.next = head
        return nodeToInsert
    
    currentNode = head
    for i in range(1,position-1):
        currentNode = currentNode.next
    nodeToInsert.next = currentNode.next 
    currentNode.next = nodeToInsert

    return head



#deleting node4(10)
head = deleteNode(node1,node4)

#creating new node to insert 
newNode = Node(7)

#inserting newnode into linkedlist at position4
head = insertInLinkedList(node1,newNode,4)

#calling traverseLinkedList function
traverseLinkedList(head)
