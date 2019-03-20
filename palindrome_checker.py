#An interesting problem that can easily be solved using deque data structure is the
#classic palindrome problem.

# A palindrome is a string that reads the same forward and backward. eg radar, toot, madam

from pythonds.basic.deque import Deque

def palchecker(aString):
	chardeque = Deque()
	
	for ch in aString:
		chardeque.addRear(ch)
		
	stillEqual = True
	
	while chardeque.size() > 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()
		if first != last:
			stillEqual = False
			
		return stillEqual
		
print(palchecker("toot"))
print(palchecker("radar"))
