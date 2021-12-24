def reverse(s):
    str=""
    print(str)
    for i in s:
        str=i+str
        print(str)
    print(len(str))
    print(str)    
    return str
    
if __name__=="__main__":
    print(reverse("Hello"))   