# a program with calculator logic

add = __import__("calc").add
sub = __import__("calc").sub
mult = __import__("calc").mult
div = __import__("calc").div
mod = __import__("calc").mod


if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter operator(+, -, *, /, %): ")

    if op == "+":
        print(add(num1, num2))
    elif op == "-":
        print(sub(num1, num2))
    elif op == "/":
        print(div(num1, num2))
    elif op == "*":
        print(mult(num1, num2))
    elif op == "%":
        print(mod(num1, num2))
    else:
        print("invalid operation")
