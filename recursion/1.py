# Program to print factorial of a number 
# recursively.
def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)

num=6

if num <0:
    print("eneter the positive value.")
elif num==0:
    print("Factorial of number 0 is 1")
else:
    print(recursive_factorial(num))       
