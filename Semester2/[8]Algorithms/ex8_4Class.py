"""LINKED LIST"""

class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

    def printNode(self):
        return '[' + self.name + ':' + str(self.age) + ']-->'


class MyList:

    def __init__(self, list):
        self.head = None

    def insert(self, name, age):
        temp = Node(name, age)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def countItems(self):
        result = 0
        temp = self.head

        while temp is not None:
            result += 1
            temp = temp.next
        return result

    def search(self, name):
        result = False
        temp = self.head

        while temp is not None:
            if temp.name == name:
                result = True
            temp = temp.next
        return result

    def printList(self):
        result = 'Head->'
        temp = self.head
        while temp is not None:
            result += temp.printNode()
            temp = temp.next
        result += 'Null'
        return result
