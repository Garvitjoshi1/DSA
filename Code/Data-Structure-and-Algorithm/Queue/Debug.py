from sys import stdin

from Data_Structure_and_Algorithm.Queues.Using_Linked_List import Queue
from Data_Structure_and_Algorithm.Stack.Using_Array import Stack


class Mystack:
    def __init__(self):
        self.insert_queue = Queue()
        self.shuffle_queue = Queue()
        self.stack_length = 0


def push(self, x: int, put=None) -> None:
    self.insert_queue(put)

    while not self.shuffle_queue.empty():
        self.insert_queue.put(
            self.shuffle_queue.get()
        )

    tem = self.insert_queue
    self.insert_queue = self.shuffle_queue
    self.shuffle_queue = tem
    self.stack_length = self.stack_length + 1

    return None


def pop(self) -> int:
    if (self.shuffle_queue.empty()):
        return 0
    else:
        item = self.shuffle_queue.get()
        self.stack_length -= 1
        return item


def top(self) -> int:
    if self.shuffle_queue.empty():
        return None
    return self.shuffle_queue.queue[0]


def isEmpty(self) -> bool:
    return self.stack_length == 0


def size(self):
    return self.size


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1