#Anagram Solution Examples with different methods.

def anagramSol(s1,s2):
	string1 = list(s1)
	string2 = list(s2)
	
	string1.sort()
	string2.sort()
	
	position = 0
	matches = True
	
	while position <len(string1) and matches:
		if string1[position] == string2[position]:
			position = position + 1
		else:
			matches = False
			print "Not anagrams"
			
	return matches
	
	
	
		
		

anagramSol("heart","earth")
