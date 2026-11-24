# a program that will raise an error

age = 16

if age < 18:
    raise ValueError("you are not elligible")
else:
    print("you voted successfully")