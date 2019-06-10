#A program that will read a string of parenthesis from left to right and
#decide whether the symbols are balanced.

#import *from stack_implementation
from pythonds.basic import Stack

def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else: 
				s.pop()
				
		index = index + 1
		
	if balanced and s.isEmpty():
		return True
	else:
		return False
		
print(parChecker('((()'))
print(parChecker('(())'))
	
