     
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def prepend(self, data):
        new = Node(data)
        if self.first is None:
            self.first = new       
        else:
            new.next = self.first
            self.first.prev = new
            self.first = new

    def append(self, data):
        new = Node(data)
        if self.first is None:
            self.first = new
        else:
            d = self.first
            while d.next is not None:
                d = d.next
            d.next = new
            new.prev = d

    def insert_after(self, target_data, data):
        new = Node(data)
        d = self.first
        while d is not None:
            if d.data == target_data:
                new.next = d.next
                new.prev = d
                if d.next is not None:
                    d.next.prev = new
                d.next = new
                return
            d = d.next

    def insert_before(self, target_data, data):
        new = Node(data)
        d = self.first
        while d is not None:
            if d.data == target_data:
                new.next = d
                new.prev = d.prev
                if d.prev is not None:
                    d.prev.next = new
                else:
                    self.first = new
                d.prev = new
                return
            d = d.next

    def delete(self, data):
        d = self.first
        while d is not None:
            if d.data == data:
                if d.prev is not None:
                    d.prev.next = d.next
                else:
                    self.first = d.next
                if d.next is not None:
                    d.next.prev = d.prev
                return
            d = d.next

    def display(self):
        d = self.first
        while d is not None:
            print(d.data, end="  ")
            d = d.next
        

linked = LinkedList()
linked.append(15)
linked.append(82)
linked.append(3)
linked.prepend(89)
linked.insert_before(3, 1)
linked.insert_after(15, 26)
linked.delete(3)
linked.display()
