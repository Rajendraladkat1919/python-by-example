# Program to calculate factorial of a number
# using a Non-Tail-Recursive function.

def nonrecursive(num):
    if num == 0:
        return 1
    else:
        return num*nonrecursive(num-1)
number=int(input("Please enter the number:"))
print("Facorial of number",number,"=",nonrecursive(number))            