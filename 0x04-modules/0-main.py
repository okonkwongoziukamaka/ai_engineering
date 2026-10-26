# a program with calculator logic

add = __import__("calc").add


if __name__ == "__main__":
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    op = input("Enter operator(+, -, *, /)")

    if op == "+":
        print(add(num1, num2))