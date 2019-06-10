#A function that takes a string as a parameter and returns a new string that 
# is the reverse of the old string.

def reverse_str(str_given):
	new_string = ""
	
	for char in str_given[::-1]:
		new_string = new_string + char 
	print new_string
	
	
reverse_str("Kofi")
