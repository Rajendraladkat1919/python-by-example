# string first programe

def first_middle_last(str):
    mid=(len(str)/2)
    return str[0]+str[mid]+str[-1]

# __name__
if __name__=="__main__":
    print(first_middle_last("hello"))