# Following is the Node class already written for the Linked List
from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNode(head, n):
    curr = head
    cnt = 0
    while curr is not None:
        if curr.data == n:
            return cnt
        cnt += 1
        curr = curr.next

    return -1


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


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    n = int(stdin.readline().rstrip())
    print(findNode(head, n))

    t -= 1
