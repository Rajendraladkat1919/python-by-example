

#read multiple number

def multi_num_sum(x,y):
	return x+y


if __name__=="__main__":
	s=input("Enter two numbers:")
	print(s)
	l=s.split()
	print(l)
	l1= [int(i) for i in l]
	a,b=l1
	print(a)
	print(b)
	print(multi_num_sum(a,b))
