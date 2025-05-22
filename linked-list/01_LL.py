class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:                     
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    
    def __str__(self):
       
        # defining a blank res variable
        res = ""
         
        # initializing ptr to head
        ptr = self.head
         
       # traversing and adding it to res
        while ptr: #while is != none
            res += str(ptr.value) + ", "
            ptr = ptr.next
 
       # removing trailing commas
        res = res.strip(", ")
         
        # chen checking if 
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

new_node = LinkedList()



for n in range(1,51):
    new_node.append(n)

new_node.append(1000)

print(new_node.head)
print(new_node.head.value)

print(new_node.tail.value)
print(new_node.length)

print(new_node)