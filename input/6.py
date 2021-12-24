#sum of float

def sum_number():
	a,b,c=[float(x) for x in input("Enter the three numbers with , sepration:").split(',')]
	return a+b+c

if __name__=="__main__":
	print(sum_number())
