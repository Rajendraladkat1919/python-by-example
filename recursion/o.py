#Program to print the fibonacci series upto n_terms

def fabseries(n):
    if n<=1:
        return n
    else:
        return(fabseries(n-1)+ fabseries(n-2))

n_terms=10

if n_terms <= 0:
    print("Invalid input !. Please provide correct validate input")
else:
    print("Below is the fabonic series!!")
    for i in range(n_terms):
        print(fabseries(i))    