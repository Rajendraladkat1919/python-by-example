#sum of number in one line

def sum():
	a,b=[int(x) for x in input("Enter the two numbers:").split()]
	print("Sum of two numbers are:",a+b)

if __name__=="__main__":
	sum()
