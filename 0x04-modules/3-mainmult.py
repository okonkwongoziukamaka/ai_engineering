# a program with calculator logic to multiply numbers

mult = __import__("calc").mult


if __name__ == "__main__":
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    op = input("Enter the Operator(+, -, *, /)")

    if op == "*":
        print(mult(num1, num2))

