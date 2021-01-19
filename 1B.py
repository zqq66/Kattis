
# Python program to demonstrate
# stack implementation using a linked list.
# node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

        # Get the current size of the stack

    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1


def StackVersion(lst):
    cards = Stack()
    for i in lst:
        card = int(i)
        if cards.getSize() != 0 and (card + cards.peek()) % 2 == 0:
            cards.pop()
        else:
            cards.push(card)
    print(cards.getSize())


def EvenUpSolitaire(lst):
    i, j = 0, 1
    result = 0
    last_i = None
    switch = False
    while i < len(lst) and j < len(lst):
        print("i", i, "j", j)
        print("last_i", last_i)
        print("switch", switch)
        print("result", result)
        if (int(lst[i]) + int(lst[j])) % 2 == 1 and j != len(lst) - 1:
            if not switch:
                last_i = i
                i += 1
                j += 1
                result += 1
                switch = True

            else:
                j = i + 1
                switch = False

        elif (int(lst[i]) + int(lst[j])) % 2 == 1 and j == len(lst) - 1:
            i += 1
            j += 1
            result += 2

        else:
            if j == last_i:
                i += 1
                j = i + 1
                result -= 1
                last_i = None

            else:
                i += 2
                j += 2
                if last_i is not None:
                    j = last_i
                    switch = True

    print(result)


if __name__ == '__main__':
    length = input()
    lst = input().split()
    # EvenUpSolitaire(lst)
    StackVersion(lst)
