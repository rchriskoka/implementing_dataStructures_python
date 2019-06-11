#A function to find minimum number in a list.
#The function compares each number to every number on the list. O(n)

import math
import time
from random import randrange


def min_num(num):
	#num = [4,7,8,6,1]
	minNum = float('inf')
	for i in num:
		if i < minNum:
			minNum = i
	return minNum
	
	
#print(min_num([2,3,5,3,2,1]))
	
#Problem solved in O(n^2) running time is shown belowe	
			
def findMin(any_list):
	minNum = any_list[0]
	for i in any_list:
		isleast = True
		for j in any_list:
			if i > j:
				isleast = False
		if isleast:
			minNum = i
	return minNum
	
#print(findMin([44,55,22,44,109,3.4,51]))
		
#Testing and showing the running times of the two functions.
for listSize in range(1000,10001,1000):
	alist = [randrange(100000) for x in range(listSize)]
	start = time.time()
	#print(min_num(alist))
	print(findMin(alist))
	end = time.time()
	print("Size %d time %f" % (listSize, end-start))

