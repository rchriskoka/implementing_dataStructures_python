#A function that simulates hotpotato game using 7 as the counting constant.

from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		simqueue.enqueue(name)
		
	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())
			
		simqueue.dequeue()
		
	return simqueue.dequeue()
	
print(hotPotato(['Brad', 'Kent', 'Jane', 'Susan', 'David', 'Bill'], 5	))

