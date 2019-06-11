"""The Node Class: the basic building block for the linked list implementation.
This code shows the implementation of an unordered list in python"""

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		
	def getData(self):
		return self.data
		
	def getNext(self):
		return self.next
		
	def setData(self, newdata):
		self.data = newdata
		
	def setNext(self, newnext):
		self.next = newnext
		
		
class UnorderedList:
	def __init__(self):
		self.head = None
		
	def isEmpty(self):
		return self.head == None
		
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		
	def size(self):
		current = self.head 
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
			
		return count
		
	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
				
				
		print found
		
	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
				
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
			
	def insert(self, new_pos, item):
		if new_pos == 1:
			new_node = Node(item)
			new_node.next = self.head
			self.head = new_node
			
		curr_pos = 1
		start_node_pos = self.head
		
		while curr_pos < new_pos and start_node_pos is not None:
			start_node_pos = start_node_pos.next
			curr_pos += 1
			
		if start_node_pos is None:
			print("Index out of Bound")
		else:
			new_node = Node(item)
			new_node.next = start_node_pos.next
			start_node_pos.next = new_node
		
		
		
		
		
	#def append(self, item):
		
	
	#def index(self, item):
		
	
	#def pop(self, item):
	
	
	
	
	
		
		
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
#print(mylist.search(18))
#print(mylist.search(100))

#mylist.add(100)
#print(mylist.search(100))
#print(mylist.size())

#mylist.remove(54)
#print(mylist.size())
#mylist.remove(93)
#print(mylist.size())
#mylist.remove(31)
#print(mylist.size())
#print(mylist.search(93))	

mylist.insert(3,56)
print(mylist.size())		
		
		
		
		
		
		
		
		
