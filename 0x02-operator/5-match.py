# a program that uses match for control flow

grade = "G"

match grade:
    case "A":
        print("excelent")
    case "B":
        print("very good")
    case "C":
        print('Good')
    case "D":
        print("Pass")
    case "E":
        print("pass")
    case "F":
        print("Fail")
    case _:
        print("grade not found")
