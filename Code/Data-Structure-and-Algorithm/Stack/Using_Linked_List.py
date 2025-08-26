from Node import Node


class Stack:
    def __init__(self):
        self.__count = None
        self.__head = None

    def __init(self):
        self.__head = None
        self.__count = 0

    def push(self, element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count + 1

    def pop(self):
        if self.isEmpty() is True:
            print("Hey!, Stack is Empty")
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count + 1
        return data

    def top(self):
        if self.isEmpty() is True:
            print("Hey!, Stack is Empty")
            return
        data = self.__head.data
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0
