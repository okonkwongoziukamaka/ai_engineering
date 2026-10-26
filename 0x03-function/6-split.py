# a program to implement a function that can split text

def splitname (fullname):
    firstname, lastname = fullname.split(" ") 
    print(firstname)
    print(lastname)

splitname("Ngozi Favour")