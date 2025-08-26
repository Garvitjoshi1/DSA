from sys import stdin

# Following is the Node class already written for the Linked List
import pkg_resources


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def appendLastNToFirst(head, n):
    if head == None or n < 0:
        return None
    c = 0
    curr = head
    prev = head
    while curr is not None and n != c:
        c += 1
        curr = curr.next
    if curr == None:
        return None
    next = curr.next
    while next is not None:
        curr = next
        next = curr.next
        prev = prev.next

    curr.next = head
    curr = prev.next
    prev.next = None
    return curr


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1
