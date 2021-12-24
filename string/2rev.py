#revers string using slice

def rev_string(s):
	return s[::-1]

if __name__=="__main__":
	s=input("Please enter the string:")
	print("orignl string is:",s)
	print("string after the reverse")
	print(rev_string(s))
