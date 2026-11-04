# a program that explains a dictionary and its applications

student = {
    "name": "Ngozi",
    "email": "okonkwongoziukamaka@gmail.com",
    "department": "Software Engineering",
    "year": 2026

}
print(student.keys())
print(student.values())
print(student["name"])
print(student.get("name"))
student.update({"level": 400, "age": 26})
print(student.items())
student.popitem()
print(student)
student.clear()
print(student)