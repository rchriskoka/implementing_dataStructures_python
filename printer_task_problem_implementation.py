"""Consider the following in  computer science laboratory. On any average day
about 10 students are working in the lab at any given hour. These students 
typically print up to twice during that time, and the length of these tasks ranges
from 1 to 20 pages. The printer in the lab is older, capable of processing 10 pages
per minute of draft quality. The printer could be switched to give better quality, but then
it would produce only five pages per minute. The slower printing speed could make students wait too long.
What page ratwe should be used.

Build a simulation that models the laboratory.

Programmer: selikem v 0.2.0
Country: Ghana
Source: interactivepython.org
"""

#To design this simulation, we will create classes for the three real-world objects
#They are: Printer, Task and PrintQueue.

from pythonds.basic.queue import Queue
import random


class Printer:
	def __init__(self, ppm): #ppm: pages per minute
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0
		
	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			if self.timeRemaining <= 0:
				self.currentTask = None
				
	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False
			
	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages() * 60/self.pagerate
		
	
class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1,21)
		
	def getStamp(self):
		return self.timestamp
		
	def getPages(self):
		return self.pages
		
	#waitTime method would be used to retrieve the amount of time spendt in the queue
	#before printing begins.	
	def waitTime(self, currenttime):
		return currenttime - self.timestamp	
	
	
def simulation(numSeconds, pagesPerMinute):
	
	labprinter = Printer(pagesPerMinute)
	printQueue = Queue()
	waitingtimes = []
	
	for currentSecond in range(numSeconds):
		
		if newPrintTask():
			task = Task(currentSecond)
			printQueue.enqueue(task)
			
		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)
			
		labprinter.tick()
		
	averageWait = sum(waitingtimes)/len(waitingtimes)
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait, printQueue.size()))
	
	
def newPrintTask():
	num = random.randrange(1,181)
	if num == 180:
		return True
	else:
		return False
		
for i in range(10):
	simulation(3600,5)
	
	
	
	
	
	
	
	
	
	
