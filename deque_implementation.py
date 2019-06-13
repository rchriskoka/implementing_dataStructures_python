"""This code shows the implementation of a Deque in python.
Deque is simply a double ended queue that combines the properties of
both stacks and queues in its implementation."""

class Deque:
	def __init__(self):
		self.items []
		
	def isEmpty(self):
		return self.items == []
		
	def addFront(self, item):
		self.items.append(item)
		
	def addRear(self, item):
		self.items.insert(0,item)
		
	def removeFront(self):
		return self.items.pop()
		
	def removeRear(self):
		return self.items.pop(0)
		
	def size(self):
		return len(self.items)
		
		
