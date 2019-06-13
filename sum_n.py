#Code to compute the sum of n numbers and showing running time

import time
#Iteration function to solve the summation problem of n numbers
def sumofN(n):
	start = time.time()
	
	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + i
		
	end = time.time()
	
	return theSum, end-start

print("Iterative Function Time")
for i in range(5):
	print("Sum of %d required %10.7F seconds"%sumofN(100000))

print("\n\n")


#Much Simpler function to do the solve the same summation problem of n numbers
def sumofN2(n):
	start = time.time()
	theSum =(n*(n+1))/2 
	
	end = time.time()
	return theSum, end-start
	
#print(sumofN2(10))
print("Recursive Function time")
for i in range(5):
	 print("Sum of %d required %10.7F seconds"%sumofN2(100000))
