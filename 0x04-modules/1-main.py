# a program with calculator logic to subtract number

sub = __import__("calc").sub


if __name__ == "__main__":
    num1 = float(imput("Enter the first number"))
    num2 = float(input("Enter the second number"))
    op = input("enter operaor(+, -, *, /)")

    if op == "-":
        print(sub(num1, num2))