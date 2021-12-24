def reverse(s):
    str=""
    for i in s:
        str=i+ str
    return str

if __name__=="__main__":
    s=input("Enter the string:")
    print("orignal string is:",s)
    print("string after reverse is",reverse(s))        
