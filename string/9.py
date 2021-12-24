#string concatation

def str_concat(str1,str2):
    return str1+str2

def str1_concat(str1,str2):
    return str1+""+str2

def str3_concat(str1,str2):
    return str1+" "+str2

if __name__=="__main__":
    print(str_concat("Hello","HI"))
    #str1_concat(True,False)
    print(str1_concat("True","False"))
    print(str1_concat("true","false"))
    print(str3_concat("Ram","Hari"))
    #str1_concat(Radha,Krishna)
    print(str1_concat("1","5"))
    #str1_concat(1,5)