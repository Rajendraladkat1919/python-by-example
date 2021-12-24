# string slicing

def string_slice(string):
	print(string[0]) # first char of string
	print(string[4]) #print 5 character of string

	print(string[0:5])

	print(string[:5])

	print(string[::])

	print(string[::2])

	print(string[::-1])

	print(string[:])
    
	for i in string:
		print(i)


if __name__=="__main__":
	string_slice("Python Basics")




